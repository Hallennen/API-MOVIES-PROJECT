from django.db import models
from actors.models import Actors
from genres.models import Genre
# Create your models here.


NATIONALITY = (
    ('BRA','Brasil'),
    ('USA','Estados Unidos')
)

class Movie(models.Model):
    title = models.CharField(max_length=500)
    year_released = models.DateField()
    actors = models.ManyToManyField(Actors, related_name='movies_actor')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies_genre')
    nationality = models.CharField(max_length=100, choices=NATIONALITY, blank=True, null=True)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    