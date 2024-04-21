from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your custom fields here
    email = models.EmailField(unique=True)
    name=models.CharField(max_length=20,blank=True,unique=False)
    profile_pic = models.ImageField(upload_to='profile_pic/', null=True, blank=True)

    class Meta:
        verbose_name = 'CustomUser'
        verbose_name_plural = 'CustomUsers'

# To avoid clash with the default User model
CustomUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'
