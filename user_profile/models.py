from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username')
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    employment_status = models.CharField(max_length=150, blank=True)
    highest_degree = models.CharField(max_length=150, blank=True)
    field_or_major = models.CharField(max_length=150, blank=True)
    about_me = models.TextField(blank=True)
    linkedin_link = models.URLField(max_length=300, blank=True)
    youtube_link = models.URLField(max_length=300, blank=True)
    twitter_link = models.URLField(max_length=300, blank=True)
    facebook_link = models.URLField(max_length=300, blank=True)    

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"
    
    