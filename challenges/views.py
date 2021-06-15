from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    "january": "January Text",
    "february": "February Text",
    "march": "MArch Text",
    "april": "April Text",
    "may": "May Text",
    "june": "June Text",
    "july": "July Text",
    "august": "August Text",
    "september": "September Text",
    "october": "October Text",
    "november": "November Text",
    "december": "December Text"
}

# Create your views here.

def index(request):
    return HttpResponse("This seems like it works!")


def february(request):
    return HttpResponse("This seems like also February works!")


def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("No URL found") 

    

def monthly_challenge_by_number(request, month):
    challenge_text = None
    if month == 1:
        challenge_text = "January"
    elif month == 2:
        challenge_text = "February"
    else:
        return HttpResponseNotFound("No URL found") 
    return HttpResponse(challenge_text)
