from django.db import models

# Create your models here.

class userinfo(models.Model):
    
    email = models.EmailField(max_length=150)
    fileinput = models.ImageField(upload_to="faces/")
  
    

    def __str__(self):
        return self.name