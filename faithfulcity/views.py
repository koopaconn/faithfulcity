from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.mail import send_mail
from . import forms

class HomePage(TemplateView):
    template_name = "index.html"

    # def get(self, request, *args, **kwargs):
    #     if request.user.is_authenticated():
    #         return HttpResponseRedirect(reverse("test"))
    #     return super().get(request, *args, **kwargs)

class HomeAbout(TemplateView):
    template_name = "about.html"

# class HomeContact(TemplateView):
#     template_name = "contact.html"

def HomeContact(request):
    if request.method == 'POST':
        form = forms.form_contact(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            sender_subject = form.cleaned_data['subject']

            message = "{0} at {1} has sent you a new message:\n\n{2}".format(sender_name, sender_email, form.cleaned_data['message'])
            send_mail(sender_subject, message, sender_email, ['koopaconn@gmail.com'],fail_silently=False,)
            form = 'Thanks for contacting us!'
            return render(request, 'contact.html', {'form': form})
    else:
        form = forms.form_contact()

    return render(request, 'contact.html', {'form': form})
