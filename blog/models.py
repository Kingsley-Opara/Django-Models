from django.db import models

from django.db.models.signals import pre_save, post_save
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone
user = get_user_model()
# Create your models here.
class Blog(models.Model):
    Author = models.ForeignKey(user, on_delete=models.CASCADE)
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Slug = models.SlugField(null=True, blank=True)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=False, auto_now=False)
    Updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (self.Title)

def blog_save(instance, save=True):
    if save:
        instance.save()

def blog_pre_save(sender, instance, *args, **kwargs):
    if instance.Slug is None:
        instance.Slug = slugify(instance.Title)
        blog_save(instance, save=False)
pre_save.connect(blog_pre_save, sender=Blog)

def blog_post_save(sender, instance, created, *args, **kwargs):
    if created:
        now = timezone.now()
        instance.Updated_date = now
        blog_save(instance, save=True)
post_save.connect(blog_post_save, sender=Blog)