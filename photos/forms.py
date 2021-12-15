from django import forms
from . import models


class SearchForm(forms.Form):
    cat_name = forms.CharField(initial="Anycat")


class FileUploadForm(forms.Form):
    class Meta:
        model = models.File

        fields = ('file')
        widgets = {
            "file": forms.ImageField(),
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
    file = forms.ImageField()

    def save(self, *args, **kwargs):
        photo = super().save(commit=False)
        cat_name = self.cleaned_data.get("cat_name")
        file = self.cleaned_data.get("file")
        photo.file = file
        photo.set_cat_name(cat_name)
        photo.save()
