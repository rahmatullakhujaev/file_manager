from django.contrib.auth.models import User
from django.db import models

class File(models.Model):
    name = models.CharField(max_length=150)
    file = models.FileField(upload_to='files/')
    owner = models.ForeignKey(User, related_name='files', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_files', blank=True)
    can_edit = models.ManyToManyField(User, related_name='editable_files', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Folder(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(User, related_name='folders', on_delete=models.CASCADE)
    files = models.ManyToManyField(File, related_name='folders', blank=True)