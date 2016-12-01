from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from apprest.models import Libro
from apprest.serializers import LibroSerializer


@csrf_exempt
def libro_list(request):
    """
    List all code libro, or create a new libro
    """
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def libro_detail(request, pk):
    """
    Retrieve, update or delete a libro
    """
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(libro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        libro.delete()
        return HttpResponse(status=204)
