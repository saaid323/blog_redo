from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=300, null=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self) -> str:
        return self.title


