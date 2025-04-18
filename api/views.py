from django.shortcuts import render
from django.http import JsonResponse
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def personList(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PersonSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    