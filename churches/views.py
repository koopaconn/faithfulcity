from django.shortcuts import render
from django.http import HttpResponse
from churches import models
from django.urls import reverse_lazy,reverse
from django.views.generic import (TemplateView,ListView,DetailView)
from django_tables2 import RequestConfig
from django_filters.views import FilterView
from .tables import ChurchTable
import django_tables2 as tables
from django_filters.views import FilterView
import django_filters
from django_tables2.views import SingleTableMixin

class ChurchFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    size = django_filters.RangeFilter()
    denomination = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.model_church
        fields = {'size','name','denomination',}

# def view_churchlist(request):
#     table = ChurchTable(models.model_church.objects.all())
#     RequestConfig(request).configure(table)
#     return render(request, 'directory_table.html', {'table': table})

class view_churchlist(SingleTableMixin,FilterView):
    table_class = ChurchTable
    model = models.model_church
    template_name = 'directory_table.html'
    filterset_class = ChurchFilter
