from django.shortcuts import render, redirect
from django.contrib.auth import logout


# TODO: refatorar para usar threads assim que possivel
def home(request):
    value1 = 10
    value2 = 20
    res = value1 / value2
    return render(request, 'home.html', {'result': res})

# FIXME: corrigir bugs
def my_logout(request):
    logout(request)
    return redirect('home')
