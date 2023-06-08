from django.db import models

class alls(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='tvshowss/images/', blank=True)
    url=models.URLField(blank=True)
    description=models.TextField()

    def __str__(self):
        return self.title
