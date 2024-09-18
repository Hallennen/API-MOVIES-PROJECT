from django.db.models.signals import pre_save
from django.dispatch import receiver
from movies.models import Movie
import json, requests

@receiver(pre_save, sender=Movie)
def movie_pre_save(sender, instance, **kwgars):
    if not instance.resume :
        instance.resume = f'''O {instance.title}, é um filme muito divertido do gênero de {instance.genre} lançado na data de {instance.year_released}; de nacionalidade {instance.nationality}. 
            '''
    
