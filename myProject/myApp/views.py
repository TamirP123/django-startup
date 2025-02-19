from django_distill import distill_path
from django.contrib import messages
from django.shortcuts import render, redirect


def home(request):
    context = {}
    return render(request, 'myApp/home.html', context)

def about(request):
    context = {}
    return render(request, 'myApp/about.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        # Testing message
        print(f"Received contact request from {name}, Email: {email}, Phone: {phone}")

        messages.success(request, "Your message has been sent successfully!")
        return redirect("home")  # Redirect to home page

    context = {}
    
    return render(request, 'myApp/contact.html', context)