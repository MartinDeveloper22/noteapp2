from django.db import models

# Create your models here.
class Author (models.Model):
    name=models.CharField(max_length=30)

    def __str__ (self):
        return self.name

class Note(models.Model):
    title=models.CharField(max_length=100)
    txt=models.CharField(max_length=100)
    authorname=models.CharField(max_length=100)#models.ForeignKey(Author,on_delete=models.CASCADE)



