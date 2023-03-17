from rest_framework import serializers

from api.models import Movie, CustomList


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CustomListSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = CustomList
        fields = '__all__'
