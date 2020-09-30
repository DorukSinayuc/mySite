from django.urls import path,include
from myPathApp import views

app_name = 'myPathApp'

urlpatterns = [
    path('',views.MyPathView.as_view(),name='mypath'),
    path('2/',views.myPathSecondPageView.as_view(),name='secondPage'),
    path('3/',views.myPathThirdPageView.as_view(),name='thirdPage'),
    path('4/',views.myPathFourthPageView.as_view(),name='fourthPage'),
    path('5/',views.myPathFifthPageView.as_view(),name='fifthPage'),
]
