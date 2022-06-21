from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


# TODO: refatorar para usar threads assim que possivel
def home(request):
    return render(request, 'home/home.html')

# FIXME: corrigir bugs
def my_logout(request):
    logout(request)
    1+1
    return redirect('home')


class HomePageView(TemplateView):
    template_name = "home2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'ola seja bem vindo ao curso de django advanced'
        return context


class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home3.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('post')
