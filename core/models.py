from django.db import models
# Create your models here.


class TimeStampModel(models.Model):
    """Time stamp Model """
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        abstract = True
