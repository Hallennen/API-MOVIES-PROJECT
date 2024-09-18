from rest_framework import serializers
from actors import models


class ActorsSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = models.Actors
        fields = '__all__'