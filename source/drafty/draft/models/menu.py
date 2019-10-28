from django.db import models

from draft.models.component import Component


class Menu(models.Model):

    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    title = models.CharField(max_length=75)
    menu = models.ForeignKey(Menu, on_delete="cascade", null=True)
    anchor = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    link = models.CharField(max_length=1064, blank=True)

    component = models.ForeignKey(Component, null=True, blank=True, on_delete="cascades")
    params = models.TextField(blank=True, help_text="Additional params to allow processing")

    icon = models.CharField(max_length=35, blank=True)
    position = models.IntegerField(default=0)
    parent = models.ForeignKey('MenuItem', null=True, on_delete=models.SET_NULL, blank=True)

    home = models.BooleanField(default=False, help_text="Is home page?")
    
    def __str__(self):
        return self.title

