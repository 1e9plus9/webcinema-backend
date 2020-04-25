from api.models import User, Movie, Comment, Genre


def run():
    User.objects.all().delete()
    Movie.objects.all().delete()
    Comment.objects.all().delete()
    Genre.objects.all().delete()
