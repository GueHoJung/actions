from django.db import models


# Create your models here.
class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
