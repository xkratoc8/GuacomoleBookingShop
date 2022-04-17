from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Posts(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    selections = models.CharField(max_length=100)
    firm_price = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    book_img = models.ImageField(upload_to="pics")
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    Author_of_book = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})


    class ebooks(models.Model):
        username = models.ForeignKey(User,on_delete=models.CASCADE)
        selection = models.CharField(max_length=100)
        year = models.CharField(max_length=100)
        Ebook_name = models.CharField(max_length=100)
        Upload_Ebook = models.FileField(upload_to='ebooks')
        date_posted = models.DateTimeField(default=timezone.now())

        def __str__(self):
            return self.Ebook_name

        def get_absolute_url(self):
            return reverse('pdf-detail', kwargs={'pk': self.pk})