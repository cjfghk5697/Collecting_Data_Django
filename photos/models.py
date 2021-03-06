import os
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from core import models as core_models
from users import models as user_models
# Create your models here.


class Photo(core_models.TimeStampModel):

    """Photo Model Definition"""
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
        choices=CAT_CHOICES, max_length=4, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("photos:detail", kwargs={"pk": self.pk})

    def first_photo(self):
        photo, = self.photos.all()[:1]
        return photo.file.url


class File(core_models.TimeStampModel):
    file = models.ImageField(upload_to="cat_photos", null=True, blank=True)
    photo = models.ForeignKey(
        "Photo", related_name="photos", on_delete=models.CASCADE)
