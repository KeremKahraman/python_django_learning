from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


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
    
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    forward_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + forward_month)

  