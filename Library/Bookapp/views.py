from django.shortcuts import render, redirect

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Bookapp.forms import RegistrationForm

def index(request):
    now = datetime.now()
    return render(request, 'Bookapp/index.html')
def about(request):   
    return render(request, 'Bookapp/about.html')

def contact(request):
    return render(request, 'Bookapp/contact.html')
def event(request):
    return render(request, 'Bookapp/event.html')

def donation(request):
    return render(request, 'Bookapp/donation.html')
    



def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/Bookapp')
        else:
            form = RegistrationForm()

            args = {'form': form}
            return render(request, 'Bookapp/register.html', args)