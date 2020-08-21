from django.conf import settings  # for date and time
from django.db import models # for creating db
from django.contrib.auth import get_user_model  # for custom model
from django.urls import reverse  # to get urls

# Create your models here.

class Code(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('code_detail', args = [str(self.id)])