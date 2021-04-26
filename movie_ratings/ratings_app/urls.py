from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, RatingViewSet, UserViewSet, TopMovieViewSet


# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('movies', MovieViewSet)
router.register('top-movies', TopMovieViewSet)

'''NOTE router.urls, app_name needs to be enclosed in tuple or error on make migrations'''

urlpatterns = [
    path('', include((router.urls, 'ratings_app'))),
]