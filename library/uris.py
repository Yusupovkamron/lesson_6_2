from django.urls import path
from .views import home, uy

urlpatterns = [
    path("home/", home),
    path("uy/", uy),

]