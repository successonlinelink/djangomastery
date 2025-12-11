from django.contrib import admin
from . import models


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "date", "image_tag")
    list_filter = ("status", "date")
    search_fields = ("title", "content")
    readonly_fields = ("pid", "date", "image_tag")

    # Display image in admin
    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="60" height="60" style="object-fit:cover; border-radius:8px;" />'
        return "No image"

    image_tag.allow_tags = True
    image_tag.short_description = "Preview"


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "phone", "date")
    search_fields = ("name", "email", "subject", "phone")
    list_filter = ("date",)
    readonly_fields = ("cid", "date")
