from django.shortcuts import render
from django.http import JsonResponse
from .models import Person
from .serializers import PersonSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Generic GET and POST view for persons
@api_view(['GET', 'POST'])
def personsList(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = PersonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Generic GET, PUT, DELETE view for a single person
@api_view(['GET', 'PUT', 'DELETE'])
def personDetailView(request, id):
    try:
        person = Person.objects.get(pk=id)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    