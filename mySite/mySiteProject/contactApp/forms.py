from django import forms

class contactFrom(forms.Form):
    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    surname = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'placeholder': 'Surname'}))
    email = forms.EmailField(label='',
                           widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    content = forms.CharField(label='',
                           widget=forms.Textarea(attrs={'placeholder': 'Content'}))
