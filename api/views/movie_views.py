from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import permissions, status

from ..models import Movie
from ..serializers import MovieSerializer
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_movies(request):
    movies = list(Movie.objects.values())
    serializer = MovieSerializer(data=movies, many=True)
    if serializer.is_valid():
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_movie(request, movie_id):
    try:
        serializer = MovieSerializer(Movie.objects.get(id=movie_id))
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response('Movie does not exist.', status=status.HTTP_404_NOT_FOUND)