from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'travello/index.html')

def about(request):
    return render(request, 'travello/about.html')

def contact(request):
    return render(request, 'travello/contact.html')

def destinations(request):
    return render(request, 'travello/destinations.html')

def elements(request):
    return render(request, 'travello/elements.html')

def news(request):
    return render(request, 'travello/news.html')    