from django.contrib import admin

# Register your models here.
from swish.models.menu import *
from swish.models.component import *
from swish.models.block import *


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass


@admin.register(ComponentAction)
class ComponentActionAdmin(admin.ModelAdmin):
    pass

