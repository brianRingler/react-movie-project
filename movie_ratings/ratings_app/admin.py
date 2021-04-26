from django.contrib import admin
from .models import Movie, Rating, TopMovie
from .imdbMovies import populate_TopMovie

'''If you do NOT want to modify/customize the admin page classes are not required
You can use: admin.site.register(TopMovie) to register model with admin site. It 
will just show a "Movie Object which is not human readable'''

# Add the table Movie, Rating and TopMovie to the admin page so it can be accessed 
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'description']
    list_filter = ['title']


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'stars']

@admin.register(TopMovie)
class TopMovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'rank', 'title', 'release_date', 'rating', 'image']
    list_filter = ['rank']


# # Call the function to populate TopMovies
try:
    if populate_TopMovie():
        print('TopMovie Table Loaded with 250 Movies!!!!')
    else:
        print('Something did not work correctly but was not an error.\nThe function populate_TopMovie evaluated false')
except Exception as e:
    print(f'There was an error: >> {e}')


