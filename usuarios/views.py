

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,TemplateView,CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from usuarios.models import Emails
# Create your views here.

class MostrarCorreos(ListView):
    template_name = "usuarios/emails_list.html"
    model=Emails
    queryset= Emails.objects.all()
    context_object_name="contextdata"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['correos'] = self.queryset
        context['mensaje'] = "hola"
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class MostrarHtmlView(TemplateView):
    template_name="basetemplate.html"