from django.db.models import fields
from rest_framework import serializers
from .models import Movie, Rating, TopMovie
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

'''
model = Movie/Rating tells django which model we are 
going to serialize.  If desired we can omit fields or 
shorthand for all is: '__all__'
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        # This is important to add.  If not added the hash password can be visible if /api/users/ is hacked
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # create a new user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # This will create the token. We do not need to return it
        token = Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'no_of_ratings', 'avg_rating']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'movie', 'user', 'stars']

class TopMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopMovie
        fields = ['id', 'image', 'title', 'release_date', 'rating']