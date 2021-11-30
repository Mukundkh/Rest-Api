from django.db import models

# Create your models here.
class Blog(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ['created_on']
