from django.db import models
from django.conf import settings

# Create your models here.
class UserEssay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = models.TextField() 
    weather = models.CharField(max_length = 10, default = 'Sunny')


class UserAlbum(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "images")
    desc = models.CharField(max_length=100)
    weather = models.CharField(max_length = 10, default = 'Sunny')

class UserFiles(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    myfile = models.FileField(blank=False, null=False, upload_to="files")
    desc = models.CharField(max_length=100)
    weather = models.CharField(max_length = 10, default = 'Sunny')

class UserWeather(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)    
    weather = models.CharField(max_length = 10, default = 'Sunny')


