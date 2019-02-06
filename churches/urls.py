from django.urls import path
from churches import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'churches'

urlpatterns = [
    path('',views.view_churchlist.as_view(),name='churchlist'),
    #path('inventory/<int:pk>/',views.view_cardetails.as_view(),name='cardetails'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
