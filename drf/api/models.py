from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class HostelPost(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/images/")
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.name
class Dante(models.Model):
    name=models.CharField(max_length=20)
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.name