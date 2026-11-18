from django.shortcuts import render

def home(request):
    return render(request, 'applications/home.html')