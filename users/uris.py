from django.urls import path
from .views import user_list, user_name

urlpatterns = [
    path("users/", user_list),
    path("user_name/", user_name)
]