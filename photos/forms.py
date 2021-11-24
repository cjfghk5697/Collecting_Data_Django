"""from typing_extensions import Required
from django import forms
from . import models
from .models import Photo


class PhotoForm(forms.Form):
    CAT_HAK = "학치"
    CAT_BBI = "삐약이"
    CAT_MOK = "목주"
    CAT_UNKNOWN = "모름"
    CAT_CHOICES = (
        (CAT_HAK, "학치"),
        (CAT_BBI, "삐약이"),
        (CAT_MOK, "목주"),
        (CAT_UNKNOWN, "모름"),
    )
    cat_name = models.CharField(
        choices=CAT_CHOICES, max_length=4, required=False)
    description = models.TextField(required=False)
    file = models.ImageField(upload_to="cat_photos",
                             null=True, blank=True, required=False)

    class Meta:
        model = Photo
        fields = ['cat_name', 'description', 'file']"""
