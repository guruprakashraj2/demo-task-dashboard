from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, dashboard, user_api

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('api/user/', user_api),
    path('api/', include(router.urls)),
]
