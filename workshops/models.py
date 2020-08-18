from django.db import models
from django.urls import reverse
from datetime import datetime, date

# Create your models here.


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField("Date (YYYY-MM-DD)*", auto_now_add=False, auto_now=False, blank=True)
    location = models.CharField(max_length=100)
    time = models.CharField(max_length=10)
    instructor = models.CharField(max_length=100)
    content = models.TextField()
    images = models.URLField(max_length=1024, null=True, blank=True)
    order =  models.CharField("Add 'order-md-first' or 'order-md-last' accordingly*", max_length=14, null=True, blank=True)
    divider =  models.CharField("Add 'workshop-divider' (Unless it\'s the last workshop one on the page)*", max_length=16, null=True, blank=True)


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('workshop-detail', kwargs={'pk': self.pk})

