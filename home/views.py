from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView


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


class HomePageView(TemplateView):
    template_name = "home2.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'ola seja bem vindo ao curso de django advanced'
        return context