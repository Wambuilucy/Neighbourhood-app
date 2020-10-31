from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class Neighbourhood(models.Model):
    name = models.CharField(max_length=144)
    location = models.CharField(max_length=144)
    occupants_count = models.PositiveIntegerField(default=0)
    police_contacts =models.PositiveIntegerField(default=0)
    health_contacts =models.PositiveIntegerField( default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE, blank=True , null=True)


    def create_neighbourhood(self):
        self.save()
        
    def delete_neighbourhood(self):
        self.delete()
        
    @classmethod
    def find_neighbourhood(cls,id):
        search = cls.objects.get(id = id)
        return  search
    
    @classmethod   
    def update_neigbourhood(cls,id,new_name):
        cls.objects.filter(pk = id).update(name=new_name)
        new_name_object = cls.objects.get(name = new_name)
        new_name = new_name_object.name
        return new_name
    
    @classmethod
    def update_occupants(cls,id,new_occupants):
        cls.objects.get(pk = id).update(occupants=new_occupants)
        new_occupants_object = cls.objects.get(pk__id = id)
        new_occupants = new_name_object.occupants
        return new_occupants
    
    def __str__(self):
        return self.name



class Business(models.Model):
    owner = models.ForeignKey(User, related_name="owners")
    name = models.CharField(max_length=144)
    email = models.EmailField(max_length=144)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, default=1)
    profile_pic = models.ImageField(upload_to='images/', default='media/images/default.jpeg')

    def create_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
        
    @classmethod
    def find_business(cls,name):
        return cls.objects.filter(title__icontains=name).all()
    
    @classmethod   
    def update_business(cls,id,new_name):
        cls.objects.filter(pk = id).update(name=new_name)
        new_name_object = cls.objects.get(name = new_name)
        new_name = new_name_object.name
        return new_name
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        ordering = ['name']

class Profile(models.Model):
    name = models.CharField(max_length=50)
    neigbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/', default='media/images/default.jpg')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    
    
    def __str__(self):
        return self.name

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()
    

class Post(models.Model):
    
    title = models.CharField(max_length=100)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neigbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    post_pic = models.ImageField(upload_to="post_pics/", blank=True)
    
    
    def create_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    @classmethod   
    def update_business(cls,id,post):
        cls.objects.filter(pk = id).update(post=post)
        new_post_object = cls.objects.filter(post__icontains = post)
        new_post = new_post_object.post
        return new_post
    
    @classmethod
    def get_single_post(cls,id):
        post = cls.objects.get(pk=id)
        return post
    
    
    def __str__(self):
        return self.title