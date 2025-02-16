from django_distill import distill_path
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'myApp/home.html', context)

def about(request):
    context = {}
    return render(request, 'myApp/about.html', context)

def contact(request):
    context = {}
    return render(request, 'myApp/contact.html', context)