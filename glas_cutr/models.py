from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


# Abstract Model
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User,on_delete=models.CASCADE)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

#Logo 
class Logo(BaseModel):
    logo_dark = models.ImageField(upload_to='images/logo', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    logo_light = models.ImageField(upload_to='images/logo', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    
    def save(self, *args, **kwargs):
        if Logo.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous logo to upload a new one!')
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.logo_light.url

#Navigation 
class Navigation(BaseModel):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def has_subnavigation(obj):
        return SubNavigation.objects.filter(navigation=obj, is_delete=False).exists()
    
    def get_subnavigation(obj):
        return SubNavigation.objects.filter(navigation=obj, is_delete=False)
    
class SubNavigation(BaseModel):
    navigation = models.ForeignKey(Navigation, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

#Home Caption & Image
class HomeCap(BaseModel):
    title_up = models.CharField(max_length=50)
    title_down = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    button_url = models.CharField(max_length=200)
    button_name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='images/home_cover', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    
    def __str__(self):
        return f'{self.title_up} {self.title_down}'
    
    def save(self, *args, **kwargs):
        if HomeCap.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous Caption to upload a new one!')
        return super().save(*args, **kwargs)

#About us 
class AboutUS(BaseModel):
    title = models.CharField(max_length=50)
    description_bold = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    button_url = models.CharField(max_length=200)
    button_name = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='images/home_cover', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    
    def __str__(self):
        return f'{self.title} {self.description_bold}'
    
    
    def save(self, *args, **kwargs):
        if AboutUS.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous About to upload a new one!')
        return super().save(*args, **kwargs)
    
#Missions
class Mission(BaseModel):
    title = models.CharField(max_length=50)
    description_bold = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    cover_image = models.ImageField(upload_to='images/home_cover', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    
    def save(self, *args, **kwargs):
        if Mission.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous Mission to upload a new one!')
        return super().save(*args, **kwargs)
    

    
    def __str__(self):
        return f'{self.title} {self.description_bold}'
    

class MissionList(BaseModel):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.text
    

#Visions
class Vision(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    cover_image = models.ImageField(upload_to='images/home_cover', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    
    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        if Vision.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous Vision to upload a new one!')
        return super().save(*args, **kwargs)
    


#Management Caption & Team
class Management(BaseModel):
    title = models.CharField(max_length=50)
    description_prev = models.CharField(max_length=50)
    description_bold = models.CharField(max_length=50)
    description_next = models.TextField(max_length=500)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if Management.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous Management to upload a new one!')
        return super().save(*args, **kwargs)
    

class Team(BaseModel):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    fb_url = models.CharField(max_length=200)
    twt_url = models.CharField(max_length=200)
    lnd_url = models.CharField(max_length=200)
    ins_url = models.CharField(max_length=200)
    profile_img = models.ImageField(upload_to='images/home_cover', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    
    def __str__(self):
        return self.name


#Services Caption & List
class Service(BaseModel):
    title = models.CharField(max_length=50)
    description_prev = models.CharField(max_length=50)
    description_bold = models.CharField(max_length=50)
    description_next = models.TextField(max_length=500)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if Service.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous Service to upload a new one!')
        return super().save(*args, **kwargs)
    
class ServiceList(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    description= models.TextField(max_length=1000)
    icon = models.ImageField(upload_to='images/icon', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    
    def __str__(self):
        return self.title
    
    @staticmethod
    def has_subservice(obj):
        return Subservices.objects.filter(service=obj, is_delete=False).exists()
    
    def get_subservice(obj):
        return Subservices.objects.filter(service=obj, is_delete=False)
    
class Subservices(BaseModel):
    service = models.ForeignKey(ServiceList,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

#Tools Image
class Tool(BaseModel):
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/icon', validators=[
        FileExtensionValidator(['jpg', 'jpeg', 'png','webp'])
    ])
    height = models.IntegerField(default=20)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.name

#Contact Infos GlasCutr Limited
class ContactInfo(BaseModel):
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    cor_office = models.CharField(max_length=200)
    can_office = models.CharField(max_length=200)
    caption = models.TextField(max_length=500)
    fb_url = models.CharField(max_length=200)
    twt_url = models.CharField(max_length=200)
    lnd_url = models.CharField(max_length=200)
    ins_url = models.CharField(max_length=200)
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if ContactInfo.objects.exists() and not self.pk:
            raise ValidationError('Delete the previous ContactInfo to upload a new one!')
        return super().save(*args, **kwargs)

#User Generated message
class UserMessage(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.email
    