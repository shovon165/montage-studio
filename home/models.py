from django.db import models
from accounts.models import User
from django.core.validators import FileExtensionValidator
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='gallary', validators=[
                               FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)


class Package(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='gallary', validators=[
        FileExtensionValidator(['png', 'jpg', 'jpeg'])], blank=False)

    totalPicture = models.IntegerField(default=300)
    editedPicture = models.IntegerField(default=50)

    price = models.IntegerField(default=2000)
    photographer = models.IntegerField(default=1)
    videographer = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(self.title)


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 254)
    phnNum  = models.BigIntegerField(default=880)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
        
    class Meta:
        ordering = ['-created']


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Contact, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


     

    def __str__(self):
        return str(self.pk)

