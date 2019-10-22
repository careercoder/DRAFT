from django.db import models


class Component(models.Model):

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    path = models.CharField(max_length=1064)  # Path Identifier
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ComponentAction(models.Model):

    component = models.ForeignKey(Component, on_delete="cascade")
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    path = models.CharField(max_length=1064)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

