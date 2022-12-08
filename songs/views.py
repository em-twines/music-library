from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Song
from serializers import SongSerializer
from rest_framework import status

@api_view(['GET'])
def songs_list(request):
    return Response('ok')



@api_view(['GET'])
def song_details(request, pk):
    try:
        song = Song.objects.get(pk = pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    except: 
        Song.DoesNotExist
        return Response(status.HTTP_404_NOT_FOUND)

# Create your views here.
