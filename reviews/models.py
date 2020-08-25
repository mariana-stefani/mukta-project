from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=45)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})
