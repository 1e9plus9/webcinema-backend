import urllib.request, os
from api.models import User, Comment, Genre, Movie
from django.core.files import File

genres = ['Adventure', 'Action', 'Animation', 'Comedy', 'Drama', 'Fantasy', 'Family', 'Science Fiction', 'Spy',
          'Superhero', 'Mystery']
movies = [
    {
        'title': 'Peter Rabbit 2',
        'release_date': '27th Mar 2020',
        'director': 'Will Gluck',
        'cast': 'James Corden, Margot Robbie, Rose Byrne, Domhnall Gleeson',
        'background': 'http://127.0.0.1:8000/media/images/movie_backgrounds/1.jpg',
        'poster': 'http://127.0.0.1:8000/media/images/movie_posters/1.jpg',
        'synopsis': 'Peter Rabbit and his bunny buddies are back, along with Bea and new husband Thomas McGregor. ' +
                    'But Peter is tired of his reputation for mischief and runs away from the'
                    + ' countryside where he bumps into an old, adventure-loving friend of his father’s. ' +
                      'James Corden, Rose Byrne, Margot Robbie, and Domhnall Gleeson reprise their roles in ' +
                      'this funny new part-animated adventure, directed by Will Gluck, ' +
                      'based on the stories by Beatrix Potter.',
        'genres': ['Family', 'Animation', 'Adventure', 'Fantasy', 'Comedy', 'Action']
    },
]


def add_genres():
    for genre in genres:
        temp = Genre()
        temp.name = genre
        temp.save()


def add_movies():
    for movie in movies:
        temp_movie = Movie()
        temp_movie.title = movie.get('title')
        temp_movie.release_date = movie.get('release_date')
        temp_movie.cast = movie.get('cast')
        temp_movie.background = movie.get('background')
        temp_movie.poster = movie.get('poster')
        temp_movie.director = movie.get('director')
        temp_movie.synopsis = movie.get('synopsis')
        temp_movie.save()

        for genre in movie.get('genres'):
            temp_genre = Genre.objects.get(name=genre)
            temp_genre.movies.add(temp_movie)


def run():
    print('here')
    add_genres()
    add_movies()
