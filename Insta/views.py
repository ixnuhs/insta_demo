from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HelloWorld(TemplateView):
    # overwrite the template_name
    template_name = 'test.html'