from django.db import models


class ImageCollection(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    image = models.ImageField(upload_to='gallery')
    collection = models.ForeignKey(ImageCollection, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.image)


class MediaCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class MediaLibrary(models.Model):
    file = models.FileField(upload_to='files', null=False, blank=False)
    category = models.ForeignKey(MediaCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    file_date = models.DateField()

    def __str__(self):
        return str(self.file).split('/')[1].replace('_', ' ')
