from django.db import models

# Create your models here.

class userimg(models.Model):
    
    fileinput = models.ImageField(upload_to="Media/")
  
    

   
