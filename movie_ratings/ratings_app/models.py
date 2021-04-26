from django.db import models

# Importing the Django User class
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.db.models.query import FlatValuesListIterable

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        avg_stars_movie = Rating.objects.filter(movie=self).aggregate(Avg('stars'))
        return avg_stars_movie['stars__avg']

    def __str__(self):
        return f"{self.id} {self.title}"

# Using ForeignKey creates a Many-to one relationship
# A rating can have one Movie and a Movie can have many Ratings 
class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User is the Django User class - Need to import 
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        # Added constraint in DB to NOT allow a Rating where the user and movie are unique together
        # If Rating is submitted with same user, same rating already in the DB it will be rejected
        unique_together = (('user', 'movie'),)
        # DB optimization will search the table faster as these fields are the main ones
        index_together = (('user', 'movie'),)
        
    def __str__(self):
        return f"{self.id} {self.movie} {self.user}  {self.stars}"

'''Top 250 movies from IMDb Rank is 1 to 250. All fields are required are raise error. Need to find way to send email if missing data on error'''
class TopMovie(models.Model):
    rank = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1),MaxValueValidator(251)],blank=False)
    # got rid of height_field=67, width_field=45
    # https://stackoverflow.com/questions/1683362/getattr-attribute-name-must-be-string-error-in-admin-panel-for-a-model-with
    image = models.ImageField(blank=False) 
    title = models.CharField(max_length=125, blank=False)
    release_date = models.CharField(max_length=4, blank=False)
    rating = models.CharField(max_length=4, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} {self.rank} {self.image} {self.title} {self.rating} {self.release_date}"









