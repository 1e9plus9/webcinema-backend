from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import permissions, status, generics

from ..models import Movie
from ..serializers import MovieSerializer
from rest_framework.response import Response


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_movie(request, movie_id):
    try:
        serializer = MovieSerializer(Movie.objects.get(id=movie_id))
        return Response(serializer.data)
    except Movie.DoesNotExist:
        return Response('Movie does not exist.', status=status.HTTP_404_NOT_FOUND)