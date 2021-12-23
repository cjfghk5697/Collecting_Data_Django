from django import forms
from django.forms.widgets import ChoiceWidget, FileInput
from django.shortcuts import redirect
from . import models


class SearchForm(forms.Form):
    cat_name = forms.CharField(initial="Anycat")


class FileUploadForm(forms.Form):
    class Meta:
        model = models.Photo

        fields = ('file')
        widgets = {
            "cat_name": forms.ChoiceField(),
            "file": forms.ImageField(),
            "description": forms.TextInput(),
        }
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
    cat_name = forms.ChoiceField(
        choices=CAT_CHOICES)
    file = forms.ImageField(widget=forms.FileInput(
        attrs={"placeholder": "File"}))
    description = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "description"}))

    def save(self, *args, **kwargs):
        model = models.Photo

        Filemodel = models.File()
        cat_name = self.cleaned_data.get("cat_name")
        description = self.cleaned_data.get("description")
        model.cat_name = cat_name
        model.description = description
        model.save()
        Filemodel.photo = models.Photo
        Filemodel.file = self.file
        Filemodel.save()
        return redirect("photos/photo_list.html")
