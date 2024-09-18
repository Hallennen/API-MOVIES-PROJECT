from django.db import models


NATIONALITY = (
    ('BRAZIL','Brasil'),
    ('USA', 'Estados Unidos'),
    ('ARG', 'Argentina'),
    ('CHI', 'Chile')
    )


# Create your models here.
class Actors(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True) 
    nationality = models.CharField(
            max_length=100,
            choices= NATIONALITY,
            blank=True,
            null=True,
        )
    
    class Meta:
        ordering= ['name']
    
    def __str__(self):
        return self.name