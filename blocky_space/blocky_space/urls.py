from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home_space.urls')),
    path('admin/', admin.site.urls),
]
