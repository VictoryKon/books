from django.core.validators import MaxValueValidator
from django.db import models


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    release = models.DateTimeField(auto_now_add=False)
    writer = models.CharField(max_length=100, blank=False, default='')
    name = models.CharField(max_length=100, blank=True, default='')
    genre = models.CharField(max_length=100, blank=False, default='')
    synopsis = models.TextField()
    price = models.PositiveIntegerField(validators=[MaxValueValidator(1000000)])

    class Meta:
        ordering = ['name']
