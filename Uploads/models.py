from django.db import models

# Create your models here.

class Articles(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    uploadfile= models.FileField(upload_to='articles/pdfs/')
    objects = models.Manager()


    def __str__(self):
        return self.name 

