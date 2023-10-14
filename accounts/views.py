from django.shortcuts import render

def login(request):
    ctx = {}
    return render(request, 'accounts/login.html', ctx)

def register(request):
    ctx = {}
    return render(request, 'accounts/register.html', ctx)
