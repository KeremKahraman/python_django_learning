from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request):
    return HttpResponse("This seems like it works!")


def february(request):
    return HttpResponse("This seems like also February works!")


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "January"
    elif month == 'february':
        challenge_text = "February"
    else:
        return HttpResponseNotFound("No URL found") 
    return HttpResponse(challenge_text)


def monthly_challenge_by_number(request, month):
    challenge_text = None
    if month == 1:
        challenge_text = "January"
    elif month == 2:
        challenge_text = "February"
    else:
        return HttpResponseNotFound("No URL found") 
    return HttpResponse(challenge_text)
