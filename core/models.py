from django.db import models
# Create your models here.


class TimeStampModel(models.Model):
    """Time stamp Model """
    created = models.DateTimeField(null=True)
    updated = models.DateTimeField(null=True)

    class Meta:
        abstract = True
