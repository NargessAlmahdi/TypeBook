from django.db import models
from django.urls import reverse

class Typeface(models.Model):
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    image = models.ImageField(upload_to='typefaces/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('typeface-detail', kwargs={'typeface_id': self.id})


class Rate(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    note = models.TextField()
    typeface = models.ForeignKey('Typeface', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_rating_display()} – {self.note[:30]}"

    class Meta:
        ordering = ['-id']
