from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # avatar = models.ImageField(upload_to="users")
    avatar = CloudinaryField("users")

    def __str__(self):
        return self.user.email


"""
{% load cloudinary %}

{% cloudinary user.userprofile.avatar  format="jpg" width=120 height=80 crop="fill" %}

https://cloudinary.com/documentation/django_image_manipulation

src="{{ MEDIA_URL }}{{ user.userprofile.avatar }}"

< img src = "https://res.cloudinary.com/dkucydb3n/image/upload/{{user.userprofile.avatar }}" class ="img-circle" alt="User Image" height = "20" width = "20" >
"""
