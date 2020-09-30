from django.urls import path,include
from contactApp import views

app_name = 'contactApp'

urlpatterns = [
    path('',views.contactView,name='contactHome'),

]
