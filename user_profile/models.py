from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=14, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='profile')

    def __str__(self):
        return self.first_name + self.last_name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()