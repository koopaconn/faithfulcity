# tutorial/tables.py
import django_tables2 as tables
from .models import model_church

class ChurchTable(tables.Table):
    class Meta:
        model = model_church
        template_name = 'django_tables2/bootstrap.html'
