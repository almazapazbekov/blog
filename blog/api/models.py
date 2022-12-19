from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post : {self.title} user : {self.user}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=256)
    date_created = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Post : {self.text[:5]} user : {self.user.name}'
