from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=20, null=False)
    telephone = models.CharField(max_length=11)
    is_admin = models.BooleanField()
    is_blocked = models.BooleanField()


class Category(models.Model):
    categoryName = models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=100)
    #requires  "pip install Pillow"
    picture = models.ImageField()
    content = models.CharField(max_length=1000)
    dateOfPublish = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=50)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


