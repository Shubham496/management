from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from django.http import HttpResponse


from .models import Task

from .serializers import TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()

    serializer_class = TaskSerializer


