from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='index_images/')


class Blog(models.Model):
    headline = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.headline

