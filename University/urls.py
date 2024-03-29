from django.contrib import admin
from django.urls import path, include
from .views import landing
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", landing),
    path("", include('library.uris')),
    path("", include('users.uris')),
]
