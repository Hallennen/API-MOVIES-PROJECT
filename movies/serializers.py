from rest_framework import serializers
from movies.models import Movie
from reviews.models import Review
from django.db.models import Sum, Avg


class MoviesSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    
    def get_rate(self, obj): 
        list_review_movie_for_id = Review.objects.filter(movie_id=obj.id)

        if list_review_movie_for_id:
            avg_for_movie = list_review_movie_for_id.aggregate(avg = Avg('stars'))['avg']
            return round(avg_for_movie,1)
        
        else:
            return 'sem avaliação.'
    

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Adaptar o resumo limitando-se a 225 caracteres.')
        return value