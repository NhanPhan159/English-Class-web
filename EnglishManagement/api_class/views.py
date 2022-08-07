from django.shortcuts import render
from api_class.models import Class
from api_class.serializers import classSerializer
from rest_framework import viewsets

# Create your views here.
class ClassModelViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = classSerializer
    