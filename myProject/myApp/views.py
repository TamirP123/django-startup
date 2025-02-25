from django_distill import distill_path
from django.contrib import messages
from django.shortcuts import render, redirect
from myApp.models import Contact


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

        # Saving data to the database
        ins = Contact(name=name, email=email, phone=phone)
        ins.save()
        print("The data has been written to the database.")

        # Testing message
        print(f"Received contact request from {name}, Email: {email}, Phone: {phone}")

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")  # Redirect to contact page with message displayed.

    context = {}
    
    return render(request, 'myApp/contact.html', context)