from django.contrib import admin
from .models import Movie, Rating, TopMovie
from .imdbMovies import populate_TopMovie

# Add the table Movie, Rating and TopMovie to the admin page so it can be accessed 
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(TopMovie)

# # Call the function to populate TopMovies
if populate_TopMovie():
    print('TopMovie Table Loaded with 250 Movies!!!!')
else:
    print('Something did not work correctly')

