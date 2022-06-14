from django.shortcuts import render, redirect
from django.contrib.auth import logout


# TODO: refatorar para usar threads assim que possivel
def home(request):
    return render(request, 'home.html')

# FIXME: corrigir bugs
def my_logout(request):
    logout(request)
    return redirect('home')
