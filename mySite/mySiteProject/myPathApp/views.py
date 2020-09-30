from django.shortcuts import render
from django.views.generic import TemplateView, View

class MyPathView(TemplateView):
    template_name = 'myPathApp/myPathPage.html'

class myPathSecondPageView(TemplateView):
    template_name = 'myPathApp/myPathPage-SecondPage.html'

class myPathThirdPageView(TemplateView):
    template_name = 'myPathApp/myPathPage-ThirdPage.html'

class myPathFourthPageView(TemplateView):
    template_name = 'myPathApp/mypathPage-FourthPage.html'

class myPathFifthPageView(TemplateView):
    template_name = 'myPathApp/myPathPage-FifthPage.html'

# Create your views here.
