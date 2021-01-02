from django.db import models
from datetime import *
from django.contrib.auth import *
from django.shortcuts import *
from ckeditor.fields import RichTextField

# Create your models here.

user = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    profile_pics = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

# adding the Post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = RichTextField(blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, auto_created=True, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def __str__(self):
        return f"{self.id} {self.title}"

    def get_absolute_url(self):
        return reverse('details', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp']

    def get_field_values(self):
        return [field.value_to_string(self) for field in Post._meta.fields]

# adding the Comment model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    name = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name


