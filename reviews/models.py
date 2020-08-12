from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friendly_name = models.CharField(max_length=50, null=False, blank=False, default='')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk})
