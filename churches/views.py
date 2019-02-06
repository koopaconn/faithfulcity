from django.shortcuts import render
from django.http import HttpResponse
from churches import models
from django.urls import reverse_lazy,reverse
from django.views.generic import (TemplateView,ListView,DetailView)

class view_churchlist(ListView):
    context_object_name = 'directory'
    model = models.model_church
    template_name = 'directory.html'
