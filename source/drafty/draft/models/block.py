from django.db import models

from .menu import MenuItem

class Block(models.Model):

    name = models.CharField(max_length=100, help_text="Friendly name of extension.")
    type = models.CharField(max_length=20, help_text="Extension Type")
    element = models.CharField(max_length=100, help_text="Unique name of the element.")
    path = models.CharField(max_length=150, help_text="Module Installed Path")

    params = models.TextField(blank=True)
    data = models.TextField(blank=True)

    enabled = models.BooleanField(default=False)
    state = models.IntegerField()
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name


class BlockMenuItem(models.Model):

    menuitem = models.ManyToManyField(MenuItem)
    block = models.ForeignKey(Block, on_delete="cascade")
    position = models.CharField(max_length=35)
    order = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)
