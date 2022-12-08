from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def songs_list(request):
    songs = Song.objects.all()
    if request.method == 'GET':
        serializer = SongSerializer(songs, many = True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    else:
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', "DELETE"])
def song_details(request, pk):
    song = get_object_or_404(Song, pk = pk)
    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(song, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    elif request.method =="DELETE":
        song.delete()
        return Response(status.HTTP_204_NO_CONTENT)



# Create your views here.
