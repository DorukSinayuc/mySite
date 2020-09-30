from django.shortcuts import render
from django.views.generic import TemplateView, View

class homePageView(TemplateView):
    template_name = 'homeApp/homePage.html'

class cvPageView(TemplateView):
    template_name = 'homeApp/cvPage.html'

class MyPathView(TemplateView):
    template_name = 'homeApp/myPath.html'

# Create your views here.
