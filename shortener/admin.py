from django.contrib import admin
from . import models


@admin.register(models.ShortLink)
class ShortLinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'short_url', 'created_at')
