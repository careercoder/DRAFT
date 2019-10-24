from django.db import models


# Register your models here.
class Article(models.Model):

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now=True, editable=True)
    def __str__(self):
        return self.title