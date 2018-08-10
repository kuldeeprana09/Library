from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def librarybanner(request):
    now = datetime.now()
    return render(
        request,
        "librarybanner.html",
        {
            'title' : "Hello Django",
            'message' : "Hello Django!",
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
   )


# Create your views here.
