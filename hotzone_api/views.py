from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView

# Create your views here.


def index(request):
    return render(request, 'index.html')

class Index(TemplateView):
    template_name = 'index.html'