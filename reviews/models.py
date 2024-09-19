from django.db import models
from movies.models import Movie
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.PROTECT, related_name = 'review_movie')
    stars = models.IntegerField(validators=[
            MinValueValidator(0, 'Não é possivel avaliar um filme com menos que 0 estrelas.'),
            MaxValueValidator(5, 'Não é possivel avaliar um filme com mais que 5 estrelas.')
        ]
    )
    comment = models.TextField(null=True, blank=True)
    date_released_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.movie}'