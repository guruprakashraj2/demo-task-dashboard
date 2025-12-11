from django.contrib import admin
from django.urls import path, include
from demo_project import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
]
