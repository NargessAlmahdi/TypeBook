from django.db import models

class Typeface(models.Model):
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    image = models.ImageField(upload_to='typefaces/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name
