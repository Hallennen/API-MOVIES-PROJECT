from django.contrib import admin
from movies.models import Movie
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','year_released', 'nationality' )

    class Meta:
        ordering = ['title']