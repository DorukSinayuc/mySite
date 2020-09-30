from django.urls import path,include
from blogApp import views

app_name = 'blogApp'

urlpatterns = [
    path('',views.MyBlogView.as_view(),name='blogHome'),
    path('1/',views.Exp2061View.as_view(),name='206-1'),
    path('2/',views.Exp2062View.as_view(),name='206-2'),
    path('3/',views.Exp2063View.as_view(),name='206-3'),
    path('4/',views.Exp2064View.as_view(),name='206-4'),
    path('5/',views.Exp2065View.as_view(),name='206-5'),
    path('6/',views.Exp2066View.as_view(),name='206-6'),
    path('7/',views.Exp2067View.as_view(),name='206-7'),
    path('8/',views.Exp2158View.as_view(),name='215-8'),
    path('9/',views.Exp2157View.as_view(),name='215-7'),
    path('10/',views.Exp2156View.as_view(),name='215-6'),
    path('11/',views.Exp2155View.as_view(),name='215-5'),
    path('12/',views.Exp2154View.as_view(),name='215-4'),
    path('13/',views.Exp2153View.as_view(),name='215-3'),
    path('14/',views.Exp2152View.as_view(),name='215-2'),
    path('15/',views.Exp2151View.as_view(),name='215-1'),
]
