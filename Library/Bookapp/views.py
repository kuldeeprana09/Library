from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    now = datetime.now()
    return render(request,
        "bookapp/index.html",
        {
            'title' : "Library App",            
            'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
        }
   )
def about(request):
   
    return render(request,
        "bookapp/about.html",
        {
            'title' : "About Library",         
        }
    )

def contact(request):
    return render(request,
                  "bookapp/contact.html",
        {
            'title' : "Contact Detail",
            'content' : "contact detail"
        }
)
def event(request):
    return render(request,
                  "bookapp/event.html",
        {
            'title' : "Event Detail",
        }

    )

def Donation(request):
    return render(request,
                  "bookapp/donation.html",
        {
            'title' : "Donation Detail",
        }

    )
    

   