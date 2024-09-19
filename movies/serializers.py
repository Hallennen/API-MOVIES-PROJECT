from rest_framework import serializers
from movies import models


class MoviesSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Movie
        fields = '__all__'

    
    def get_rate(self, obj):
        
        return 5
    

    def validate_resume(self, value):
        if len(value) > 225:
            raise serializers.ValidationError('Adaptar o resumo limitando-se a 225 caracteres.')
        return value