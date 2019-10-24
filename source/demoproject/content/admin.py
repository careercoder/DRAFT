from django.contrib import admin

from content.models import *


@admin.register(Article)
class ContentAdmin(admin.ModelAdmin):
    pass
