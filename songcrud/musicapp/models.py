from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(Max_lenght = 200)
    Last_name = models.CharField(Max_lenght = 200)
    age = models.IntergerField(Max_lenght = 10)

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(Max_length = 200)
    date_released = models.DateTimeField(Max_lenght = 100)
    likes = models.IntergerField(Max_lenght = 10)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class lyrics(models.Model):
    content = models.TextField(Max Max_lenght 2000)
    song_id = models.ForeignKey(song, on_delete=models.CASCADE)
    