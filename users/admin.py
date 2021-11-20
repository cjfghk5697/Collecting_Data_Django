from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "stu_id",
        "name",
        "email",
        "phone_number",
        "member",
    )
    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "member",
                ),
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("member",)
