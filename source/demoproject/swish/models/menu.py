from django.db import models


class Menu(models.Model):

    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):

    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=75)
    anchor = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    link = models.CharField(max_length=1064, blank=True)

    app = models.CharField(max_length=150, blank=True, help_text='The App this is Connected To')
    action = models.CharField(max_length=150, blank=True, help_text='The action this is connected to within the app')
    params = models.TextField(blank=True, help_text="Additional params to allow processing")

    icon = models.CharField(max_length=35, blank=True)
    position = models.IntegerField(default=0)
    parent = models.ForeignKey('MenuItem', null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.title

