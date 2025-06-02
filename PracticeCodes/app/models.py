from django.db import models
from django.utils import timezone

# Create your models here.
class App(models.Model):
    APP_TYPE =[
        ('SC', 'SnapChat'),
        ('IN', 'InstaGram'),
        ('WP', 'WhatsApp'),
        ('FB', 'FaceBook')
    ]
    name= models.CharField(max_length=30)
    img = models.ImageField(upload_to='dashboard/')
    date= models.DateTimeField(default=timezone.now)
    type= models.CharField(max_length= 2, choices=APP_TYPE)
    description= models.TextField(default='')

    def __str__(self):
      return self.name


