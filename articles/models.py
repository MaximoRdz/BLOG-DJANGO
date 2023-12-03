from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    abstract = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail_image = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.title    
