


from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 


from .views import WebXml


urlpatterns = [
 path('', TemplateView.as_view(template_name='accreate/home.html')), 
 path('admin/', admin.site.urls),
 path("xmlwebr",WebXml.webxmlR,name="xmlwebr")


]