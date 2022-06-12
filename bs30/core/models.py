from django.db import models

# Create your models here.
class NewUserTB(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)
    
