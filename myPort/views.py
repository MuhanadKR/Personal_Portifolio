from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "home.html", {})

def about(request):
    return render(request, "about.html", {})

def contact(request):
    return render(request, "contact.html", {})

def projects(request):
    return render(request, "projects.html", {})

def rhino(request):
    return render(request, "rhino.html", {})

def clipboard(request):
    return render(request, "clipboard.html", {})

def security(request):
    return render(request, "security.html", {})

def portifolio(request):
    return render(request, "portifolio.html", {})