import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from genres import models
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from genres.serializers import GenreSerializer



class GenerCrateListView(ListCreateAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = GenreSerializer




class GenreUpdateDeleteDetail(RetrieveUpdateDestroyAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = GenreSerializer





# Create your views here.
# @csrf_exempt
# def genre_view(request):
#     if request.method == 'GET':

#         genres = models.Genre.objects.all()
#         data = [{'id': genre.id , 'name': genre.name} for genre in genres]

#         return JsonResponse(data, safe=False)

#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = models.Genre(name=data['name'])
#         new_genre.save()

#         return JsonResponse(
#             {'id': new_genre.id, 'name': new_genre.name},
#             status=201,
#             )
    

# @csrf_exempt
# def detail_genre(request, pk):
#     genre = get_object_or_404(models.Genre, pk=pk)

#     if request.method == "GET":
#         data = {'id': genre.id, 'name':genre.name}
#         return JsonResponse(data)

#     elif request.method == 'DELETE':
#         genre.delete()
#         return JsonResponse({'message': f'Id {pk} exluido'},status=204)
    
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = data['name']
#         genre.name = new_genre
#         genre.save()
#         return JsonResponse({'message:': f'Id {pk} atualizado'})
    
