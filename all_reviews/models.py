from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

class alls(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='tvshowss/images/', blank=True)
    url=models.URLField(blank=True)
    description=HTMLField()

    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title
