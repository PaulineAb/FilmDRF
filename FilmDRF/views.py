from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from imdb import Cinemagoer

from drfapp.serializers import UserSerializer, FilmSerializer
from drfapp.models import User, Film

class UserView(ModelViewSet):

  serializer_class = UserSerializer

  def get_queryset(self):
    users = User.objects.all()
    login = self.request.GET.get('login')
    password = self.request.GET.get('password')
    if login is not None:
      users = users.filter(name=login)
      if password is not None:
        users = users.filter(password=password)
        return users
    return []

class FilmView(ModelViewSet):

  serializer_class = FilmSerializer

  def get_queryset(self):
    films = Film.objects.all()
    userlist = self.request.GET.get('userlist')
    if userlist is not None:
      films = films.filter(userlist=userlist)
      return films
    return []

class SearchView(APIView):

  def get(self, request, *args, **kwargs):
    ia = Cinemagoer()
    searchword = self.request.GET.get('searchword')
    movies = ia.search_movie(searchword)
    for movie in movies:
      movie['movieID'] = movie.movieID
    return Response(movies)

class SearchDetailsView(APIView):

  def get(self, request, *args, **kwargs):
    ia = Cinemagoer()
    movieId = self.request.GET.get('movieid')
    movie = ia.get_movie(movieId)
    return Response(movie)

class AddFilmView(APIView):

  def post(self, request, *args, **kwargs):
    serializer = FilmSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)
