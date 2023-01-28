from django.db import models

# Create your models here.
LANGUAGES = {"en":"English","fr":"French"}

class Language(models.Model):
   code = models.CharField(max_length=7, primary_key=True)
   language = models.CharField(max_length=100)
 
   def __str__(self):
       return f'{self.code}'

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=False, null=True)
    title = models.TextField()

    def __str__(self):
        return self.title
