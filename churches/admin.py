from django.contrib import admin
from churches.models import model_church,model_churchpic

# Register your models here.
admin.site.register(model_church)
admin.site.register(model_churchpic)
