from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class CaseAddView(TemplateView):
    template_name = 'case.html'

class VistedLocationAddView(TemplateView):
    template_name = 'visitedlocation.html'

class VirusAddView(TemplateView):
    template_name = 'virus.html'