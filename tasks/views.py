from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
import requests

# CRUD API for Tasks
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Fix CSRF issue for demo frontend
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

# Dashboard view
def dashboard(request):
    return render(request, 'tasks/dashboard.html')

# User API integration
@api_view(['GET'])
def user_api(request):
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users/1')
        return Response(response.json())
    except Exception as e:
        return Response({"error": str(e)})
