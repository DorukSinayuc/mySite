from django.urls import path,include
from homeApp import views

app_name = 'homeApp'

urlpatterns = [
    path('',views.homePageView.as_view(),name='home'),
    path('CV/',views.cvPageView.as_view(),name='cv'),
    # path('MyPath/',include('myPathApp.urls'),name='MyPath')
]
