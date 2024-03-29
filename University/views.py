from django.http import HttpResponse

def landing(requset):
    return HttpResponse("Hi lazy developers")