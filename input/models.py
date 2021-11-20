import os
from django.db import models

from core import models as core_models
from users import models as user_models

# Create your models here.


class Inputs(core_models.TimeStampModel):
    """Input Model Definition"""
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
    cat_name = models.CharField(choices=CAT_CHOICES, max_length=2, blank=False)
    description = models.TextField()
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)


class Photo(core_models.TimeStampModel):
    """Photo Model Definition"""
    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey(Inputs, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
