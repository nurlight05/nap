from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from math import ceil
from django.template.defaultfilters import truncatechars

class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, blank=False, unique=True)
    body = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to="img/articles/%Y/%m/%d", default="img/articles/default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_at"]
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("show_article_blog", kwargs={"slug": self.slug})
    
    @property
    def reading_time(self):
        words_count = len(self.body.split())
        reading_time = ceil(words_count / 265)
        return f"{reading_time} мин"
    
    @property
    def short_description(self):
        return truncatechars(self.body, 35)
    
