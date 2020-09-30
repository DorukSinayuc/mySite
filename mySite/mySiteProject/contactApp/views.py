from django.shortcuts import render
from django.views.generic import TemplateView, View
from contactApp import forms
from mySiteProject.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def contactView(request):
    form = forms.contactFrom()

    if request.method == 'POST':
        form = forms.contactFrom(request.POST)
        subject = str(form['name'].value())+" has reached out"
        message = str(form['content'].value())+" Email of sender: " +str(form['email'].value())
        recepient = EMAIL_HOST_USER
        name = str(form['name'].value())

        send_mail(subject,message,EMAIL_HOST_USER,[EMAIL_HOST_USER],fail_silently=False)
        return render(request,'contactApp/contactSuccessPage.html',{'name': name})

    return render(request,'contactApp/contactPage.html',{'form': form})





# class contactView(TemplateView):
#     template_name = 'contactApp/contactPage.html'
# Create your views here.
