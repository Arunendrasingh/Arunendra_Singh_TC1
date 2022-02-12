from django.shortcuts import redirect, render
from TC_1.models import *
import datetime
from django.contrib import messages

# Create your views here.

def index(request):
    add_obj = Address_info.objects.all()
    return render(request, 'Address_Book.html', {'address_detail': add_obj})

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
        First_name = request.POST['first_name']
        Last_name = request.POST['last_name']
        street_name = request.POST['street']
        city_name = request.POST['city_name']
        zip_code = request.POST['zip_code']
        user_email = request.POST['user_email']
        address_obj = Address_info(first_name = First_name, last_name = Last_name, street = street_name, zip_code = zip_code, city_name = city_name, user_email=user_email)
        address_obj.save()

        # Extract the data and show it on page
        add_obj = Address_info.objects.all()
        return render(request, 'Address_Book.html', {'address_detail': add_obj})
    else:
        return render(request, 'Address_form.html', {'city_name':city_obj})


def delete_address(request, id):
    p_obj = Address_info.objects.get(id = id)
    p_obj.delete()
    messages.info(request, "Address Information of " +p_obj.first_name + " " + p_obj.last_name+" is Deleted Succesfully!")
    return redirect("/")

def edit_address(request, id):
    if request.method == 'POST':
        p_obj = Address_info.objects.get(id = id)
        p_obj.first_name = request.POST['first_name']
        p_obj.last_name = request.POST['last_name']
        p_obj.street = request.POST['street']
        p_obj.zip_code = request.POST['zip_code']
        p_obj.city_name = request.POST['zip_code']
        p_obj.user_email = request.POST['user_email']
        p_obj.save()
        messages.info(request, "Address Information of " +p_obj.first_name + " " + p_obj.last_name+" is Edited Succesfully!")
        return redirect("/")   
    else:
        city_obj = City.objects.all()
        p_obj = Address_info.objects.get(id = id)
        return render(request, 'Address_form.html', {'city_name':city_obj, 'address_obj': p_obj, 'editable':1})
    
