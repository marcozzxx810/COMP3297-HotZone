"""hotzone_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hotzone_api.views import CaseAddView, VistedLocationAddView, IndexView, VirusAddView
from case_record.views import CaseRecordView
from visited_location.views import VisitedLocationView
from virus.views import VirusView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('caseadd/', CaseAddView.as_view(), name='caseadd'),
    path('vlocationadd/', VistedLocationAddView.as_view(), name='visitedlocationadd'),
    path('virusadd/', VirusAddView.as_view(), name='virusadd'),
    path('caserecord/', CaseRecordView.as_view(), name='caserecord'),
    path('visitedlocation/', VisitedLocationView.as_view(), name='visitedlocation'),
    path('virus/', VirusView.as_view(), name='virus'),
]
