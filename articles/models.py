import os
from django.db import models


def get_upload_path_thumbnail(instance, filename):
    return os.path.join("images", str(instance.slug), filename)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    abstract = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumbnail_image = models.ImageField(upload_to=get_upload_path_thumbnail, 
                                        default="default.png", 
                                        blank=True)
    
    def __str__(self):
        return self.title    
    

def get_upload_path_images(instance, filename):
    return os.path.join("images", str(instance.post.slug), filename)

class PostImage(models.Model):
    post = models.ForeignKey("Post", related_name="images", on_delete=models.PROTECT)
    image = models.ImageField(upload_to=get_upload_path_images, 
                              default="default.png", blank=True)



