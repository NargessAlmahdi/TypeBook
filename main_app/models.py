from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Typeface(models.Model):
    CLASSIFICATION_CHOICES = [
        ('Serif', 'Serif'),
        ('Sans Serif', 'Sans Serif'),
        ('Slab Serif', 'Slab Serif'),
        ('Display', 'Display'),
        ('Script', 'Script'),
        ('Monospace', 'Monospace'),
        ('Handwritten', 'Handwritten'),
        ('Blackletter', 'Blackletter'),
    ]
        
    name = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    classification = models.CharField(max_length=100, choices=CLASSIFICATION_CHOICES)
    image = models.ImageField(upload_to='typefaces/')
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('typeface-detail', kwargs={'typeface_id': self.id})


class Rating(models.Model):
    RATING_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    typeface = models.ForeignKey(Typeface, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'typeface') 

    def __str__(self):
        return f"{self.user.username} – {self.get_rating_display()}"


class Note(models.Model):
    note = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    typeface = models.ForeignKey(Typeface, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} – {self.note[:30]}"

    class Meta:
        ordering = ['-created_at']



class Pairing(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pairings/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pairing-detail', kwargs={'pk': self.id})
