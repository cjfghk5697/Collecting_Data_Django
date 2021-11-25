from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "cat_name",
        "__str__",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "photo",
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
