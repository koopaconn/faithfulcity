from django.shortcuts import render
from django.http import HttpResponse
from churches import models
from django.urls import reverse_lazy,reverse
from django.views.generic import (TemplateView,ListView,DetailView)
from django_tables2 import RequestConfig
from .tables import ChurchTable

# class view_churchlist(ListView):
#     context_object_name = 'directory'
#     model = models.model_church
#     template_name = 'directory.html'

# class view_churchlist(ListView):
#     context_object_name = 'directory'
#     model = models.model_church
#     template_name = 'directory.html'
#     paginate_by = 25
#     queryset = model.objects.all()

def view_churchlist(request):
    table = ChurchTable(models.model_church.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'directory_table.html', {'table': table})

# class view_churchlist(SingleTableMixin, FilterView):
#     table_class = ChurchTable
#     model = models.model_church
#     template_name = 'directory_table.html'
