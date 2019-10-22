from django.db import models


class Component(models.Model):

    name = models.CharField(max_length=150)
    path = models.CharField(max_length=1064)

    def __str__(self):
        return self.name


