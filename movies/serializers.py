from rest_framework import serializers
from movies import models


class MoviesSerializers(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = '__all__'