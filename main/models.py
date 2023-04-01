from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.contrib.auth.models import User
import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.

#City
class city(models.Model):
    city_name =models.CharField(max_length=32)
    
    def __str__(self):
        return self.city_name


##Station
class Station(models.Model):
    station_Id =models.AutoField(primary_key=True)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    stationName=models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    
    def __str__(self):
        return self.stationName

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make('http://127.0.0.1:8000')
        canvas = Image.new('RGB', (290, 290), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.stationName}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class Category(models.Model):
    categ= models.CharField(max_length=40)
      
    def __str__(self):
        return self.categ

class FeedbackForm(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.EmailField()
    city=models.ForeignKey(city, on_delete=models.SET_NULL, blank=True, null=True)
    station=models.ForeignKey(Station,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField()
   # image=models.ImageField(upload_to = "images/") 

    def __str__(self):
         return f'Name: {self.name} || Police station: {self.station} || Category:{self.category} '
    

class Profile(models.Model):
    username = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=13)
    otp =models.CharField(max_length=100,null=True,blank=True)
    uid= models.UUIDField(default=uuid.uuid4)