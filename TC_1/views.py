from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Contact(request):
    return render(request, 'Contact_Us.html')

def Address_Book(request):
    return render(request, 'Address_Book.html')
