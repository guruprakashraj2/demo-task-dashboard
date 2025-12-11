from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .models import Task
from .serializers import TaskSerializer
import requests


@method_decorator(csrf_exempt, name='dispatch')
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # FIXED: PATCH / COMPLETE BUTTON NOW WORKS
    def partial_update(self, request, *args, **kwargs):
        task = self.get_object()

        # Only update fields provided
        for field, value in request.data.items():
            setattr(task, field, value)

        task.save()
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


def dashboard(request):
    return render(request, 'tasks/dashboard.html')


@api_view(['GET'])
def user_api(request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/users/1")
        return Response(response.json())
    except Exception as e:
        return Response({"error": str(e)})
