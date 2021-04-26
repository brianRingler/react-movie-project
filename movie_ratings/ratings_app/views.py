from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Movie, Rating, TopMovie
from .serializers import MovieSerializer, RatingSerializer, UserSerializer, TopMovieSerializer

'''
https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset

ModelViewSet inherits from GenericAPIView and includes a few options to use: .list(), .retrieve(), .create(), .update(), .partial_update() and .destroy().   We can also create our own custom method.
'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    # Create a custom method 
    # https://www.django-rest-framework.org/api-guide/responses/

    # decorator is required to tell django this method is an action and that it is used for POST only
    # detail=True means user needs to provide specific movie
    
    # We use the movie id to specify the movie we want. By default the pk is passed and b/c it is not being used causes error. Thus, pk=None is used to resolve error.

    # "request.data" returns the parsed content of the request body. This is similar to the standard request.POST and request.FILES attributes except that:see docs
    # https://www.django-rest-framework.org/api-guide/requests/
    @action(detail=True, methods=['POST'])
    def rate_movie(self, request, pk=None):
        if 'stars' in request.data and int(request.data['stars']) >= 1 and int(request.data['stars']) <= 5:

            movie = Movie.objects.get(id=pk)
            # How many stars did the user rate this movie
            stars = request.data['stars']

            # .user returns instance of django.contrib.auth.models.User. If token is not used (unauthenticated) the default value is AnonymouseUser
            user = request.user
            print('---------++++----------')
            print(user)
            # user = User.objects.get(id=3)

            try:
                # If no rating for this user and movie this line will fail
                rating = Rating.objects.get(id=user.id, movie=movie.id)
                rating.stars = stars
                rating.save()

                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except:
                # Create rating for this movie by this user
                rating = Rating.objects.create(user=user, movie=movie, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)

            # https://www.django-rest-framework.org/api-guide/viewsets/
        else:
            response = {'message': 'You need to provide a star rating 1 - 5'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer    
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    # In the MovieViewSet we created an @action that allows user to:
    # - Update the Movie rating which is in the 'try' block
    # - Create a rating if there is already not a rating for that movie by active user
    # Thus, the below two functions will prevent updating and creating a rating
    # They must use "rate_movie" http://127.0.0.1:8000/api/movies/2/rate_movie/
    def update(self, request, *args, **kwargs):
        response = {'message': 'To update a rating use /api/movies/[id]/rate_movie/'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'To create a rating use /api/movies/[id]/rate_movie/'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

# The Top 250 movies IMBd
class TopMovieViewSet(viewsets.ModelViewSet):
    queryset = TopMovie.objects.all()
    serializer_class = TopMovieSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)