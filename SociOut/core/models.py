from django.db import models
from django.contrib.auth import get_user_model
import uuid #helps us to generate unique tokens/ids
from datetime import datetime

User = get_user_model()
# now we would use this model to create every new profile

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # this is going to be the foriegn key
    # for refernce to on-delete and CASCADE refer: https://docs.djangoproject.com/en/stable/ref/models/fields/#django.db.models.ForeignKey.on_delete
    """CASCADE: When the referenced object is deleted, also delete the objects that have references to it 
        (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
    """
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='profile_images', default='default_img.png')
    # because django has access to the media folder only
    location = models.CharField(max_length=100, blank=True) 

    def __str__(self):
        return self.user.username
        """ 'username' will be shown as the field name in the database from the admin panel"""
    

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4)
    user = models.CharField(max_length=100) #owner of the post
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user #because it is not foriegn key
        """ if it were a foriegn key it becomes an object and so we need to return differently """

class LikePost(models.Model):
    post_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
        

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user