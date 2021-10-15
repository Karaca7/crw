from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from django.forms import ModelForm

from django.core.files.uploadedfile import InMemoryUploadedFile   

from io import BytesIO

from .models import Catalog


class  CForm(ModelForm):

    class Meta:
        model= Catalog
        fields=['common','botanical','zone','light','price','acaıkabıkıty']

