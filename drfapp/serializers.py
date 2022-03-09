from rest_framework import serializers
from .models import User, Film

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'name', 'password']

class FilmSerializer(serializers.ModelSerializer):
  class Meta:
    model = Film
    fields = [
      'id',
      'title',
      'poster',
      'duration',
      'year',
      'director',
      'producer',
      'actors',
      'synopsis',
      'userlist'
    ]
