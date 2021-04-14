from django.db import models
from PIL import Image
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
User = get_user_model()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='images/profile_pics/%Y/%m/%d')
    image_thumbnail = ImageSpecField(
                            source='profile_picture',
                            processors=[ResizeToFill(300,300)],
                            format='JPEG',
                            options={'quality':80})
    bio = models.TextField()
    phone = models.CharField(max_length=13)
    tel_no = models.CharField(max_length=10)
    slug = models.SlugField(blank=True)
    
    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super(Profile, self).save(*args, **kwargs)
    
    
class PhoneDb(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    otp = models.IntegerField(null=True)
    is_verified = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.phone}"
    
    class Meta:
        verbose_name = "Phone Database"
        verbose_name_plural = "Phone Databases"
    