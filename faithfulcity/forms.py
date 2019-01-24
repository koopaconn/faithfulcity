from django import forms

class form_contact(forms.Form):
    name  = forms.CharField(label='Your name', max_length=100)
    email  = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
