from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Inputs)
class InputAdmin(admin.ModelAdmin):
    list_display = (
        "cat_name",
        "decription",
        "host"
    )

    fieldsets = (
        (
            "Cat Profile",
            {
                "fields": (
                    "cat_name",
                ),
            },
        ),
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
