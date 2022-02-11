from django.shortcuts import render
from TC_1.models import *
import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    city_obj = City.objects.all()
    return render(request, 'Address_Book.html')

def Contact(request):
    if request.method  == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_message = request.POST['message']
        user_obj = Contact_Info(Name = user_name, email= user_email, message=user_message, issue_date=datetime.datetime.now())
        user_obj.save()
        messages.info(request, "Your message was sent, thank you!")
        return render(request, 'Contact_Us.html')
    else:
        return render(request, 'Contact_Us.html')

def Address_Book(request):
    city_obj = City.objects.all()
    if request.method  == 'POST':
        return render(request, 'Address_Book.html')
    else:
        return render(request, 'Address_form.html', {'city_name':city_obj})
