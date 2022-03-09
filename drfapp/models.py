from django.db import models

class User(models.Model):
  name = models.CharField(max_length=100)
  password = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Film(models.Model):
  
  title = models.CharField(max_length=100)
  poster = models.TextField()
  duration = models.CharField(max_length=100)
  year = models.CharField(max_length=100)
  director = models.JSONField()
  producer = models.JSONField()
  actors = models.JSONField()
  synopsis = models.TextField()
  userlist = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.title