from django.contrib import admin 
from django.urls import path, include

urlpatterns = [
    path('', include('api_rest.urls')),  
    path('admin/', admin.site.urls), 
]
