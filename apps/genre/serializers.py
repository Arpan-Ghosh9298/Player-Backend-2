from .models import Genre
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(allow_null=True)

    class Meta:
        model = Genre
        fields = '__all__'