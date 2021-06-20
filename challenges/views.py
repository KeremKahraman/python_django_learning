from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse


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
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
        list_items += "<tr/>"

    response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)


def monthly_challenge(request, month):
    
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge_month" : month.capitalize(),
            "challenge_text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>No URL found</h1>") 
    

def monthly_challenge_by_number(request, month):
    
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    
    forward_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[forward_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

  