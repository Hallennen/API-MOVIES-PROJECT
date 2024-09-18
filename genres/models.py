from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    
