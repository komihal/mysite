from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def projects_view(request):
    return render(request, 'projects.html')

def services_view(request):
    return render(request, 'services.html')