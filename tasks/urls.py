from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, dashboard, user_api
from demo_project import settings

# Router for CRUD operations
router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('api/', include(router.urls)),
    path('api/user/', user_api, name='user'),  # New API
]
