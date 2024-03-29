from django.shortcuts import render
from django.http import HttpResponse
def user_list(request):
    return HttpResponse("this is user page")
def user_name(request):
    return HttpResponse("this ish user_name")