from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.utils import timezone
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None, *args, **kwargs
    ):
        super().save(*args, **kwargs)
##
# img = Image.open(self.image.path)

# if 300 > img.height or img.width > 300:
#   output_size = (300, 300)
#  img.thubmnail(output_size)
# img.save(self.image.path)

# class Pdfs(models.Model):
# username = models.ForeignKey(User,on_delete=models.CASCADE())
# branch = models.CharField(max_length=100)
# year = models.CharField(max_length=20)
# pdf_name = models.CharField(max_length=100)
# firm_price = models.CharField(max_length=100)
# op_price = models.CharField(max_length=100)
# date_posted = models.CharField(max_length=20)
# pdf_name = models.CharField(max_length=100)
# email = models.CharField(max_length=100)
