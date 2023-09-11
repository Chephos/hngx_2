from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ValidationError

from . import serializers
from . import workers
# Create your views here.


class PersonCreate(APIView):
    def get(self, request):
        return Response({"message":"why not create new persons on here and get what it feels like to be God:)"})

    def post(self, request):
        name = request.data.get("name")
        if  not isinstance(name, str):
            raise ValidationError("Name value must be a string")
        
        serializer = serializers.Person(data=request.data)
        serializer.is_valid(raise_exception=True)
        person = workers.Person.create_person(serializer.validated_data)

        return Response({"id": person.id, "name": person.name}, status=status.HTTP_201_CREATED)
    
class PersonDetail(APIView):
    def get(self, request, pk=None):
        person = workers.Person.get_person(pk)
        if person is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = serializers.Person(person)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk):
        serializer = serializers.Person(data=request.data)
        serializer.is_valid(raise_exception=True)
        person = workers.Person.update_person(pk, serializer.validated_data)
        if person is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk):
        person = workers.Person.delete_person(pk)
        if person is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"message":"Person successfully cut off, cheers!"},status=status.HTTP_204_NO_CONTENT)


