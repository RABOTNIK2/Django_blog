from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
    image = models.TextField(default="https://avatars.mds.yandex.net/i?id=615d51cbb0baad8f3a4763e761b597eceaea56bc-11269055-images-thumbs&n=13")
    friends = models.ManyToManyField('self', symmetrical=False, related_name='friend_set', blank=True)
    
    def add_friend(self, user):
        if user != self and not self.friends.filter(id=user.id).exists():
            self.friends.add(user)
            self.save()
            return True
        return False
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

class Theme(models.Model):
    name = models.CharField(max_length=40)
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    images = models.TextField(blank=True, null=True)
    posted_at = models.DateField(default=datetime.date)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)
    
class Favorite(models.Model):
    user_fav = models.ForeignKey(User, on_delete=models.CASCADE)
    post_fav = models.ManyToManyField(Post)
    
class Comment(models.Model):
    autho_of_comm = models.ForeignKey(User, on_delete=models.CASCADE)
    post_to = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    picture = models.TextField(blank=True, null=True)
    make_at = models.DateField(default=datetime.date)
    
       
    
    

# Create your models here.
