from django.contrib import admin

from .models.component import *
from .models.block import *

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    pass

@admin.register(BlockMenuItem)
class BlockMenuItemAdmin(admin.ModelAdmin):
    pass