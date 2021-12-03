from django import forms
from . import models


class SearchForm(forms.Form):
    cat_name = forms.CharField(initial="Anycat")
