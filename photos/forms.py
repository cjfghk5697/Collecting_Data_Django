from django import forms
from . import models


class SearchForm(forms.Form):
    cat = forms.CharField(initial="Anycat")
