from django.shortcuts import render
from rest_framework import viewsets
from product.models import Person
from product.serializers import PersonSerializer


# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
