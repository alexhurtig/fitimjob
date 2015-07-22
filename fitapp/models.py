from django.core.files.storage import get_storage_class
from django.db import models

# Create your models here.
from fitimjob import settings


def getImages(self):
    static_storage = get_storage_class(settings.STATICFILES_STORAGE)()
    directories, files = static_storage.listdir('images')
    return [
        static_storage.url('images/' + file)
        for file in files
        if file.startswith(self.name) and file.endswith('.jpg')
        ]

def getVideos(self):
    static_storage = get_storage_class(settings.STATICFILES_STORAGE)()
    directories, files = static_storage.listdir('videos')
    return [
        static_storage.url('videos/' + file)
        for file in files
        if file.startswith(self.name) and file.endswith('.mp4')
        ]