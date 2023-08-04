from rest_framework import generics
from .serializers import GenreSerializer
from .models import Genre
# Create your views here.
class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.order_by('-created_at').all()
    serializer_class = GenreSerializer

