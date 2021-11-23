import os
from django.db import models

from core import models as core_models
from users import models as user_models

# Create your models here.


class Input(core_models.TimeStampModel):
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
    cat_name = models.CharField(choices=CAT_CHOICES, max_length=4)
    description = models.TextField()
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="cat_photos", null=True, blank=True)

    def __str__(self):
        return self.description
