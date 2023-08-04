from rest_framework import generics
from .models import Song
from django.http import HttpResponse
from .serializers import SongSerializer
# Create your views here.

class SongList(generics.ListCreateAPIView): #to handle the get request and handle the documents list
    queryset = Song.objects.all()
    serializer_class=SongSerializer

class SongDetail(generics.RetrieveUpdateAPIView):  #we can recover and update the details here with the generics actions
    queryset = Song.objects.all()
    serializer_class = SongSerializer    

