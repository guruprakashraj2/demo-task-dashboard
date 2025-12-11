from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, dashboard, user_api

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', dashboard, name='dashboard'),
    path('api/user/', user_api, name='user_api'),
]
