from django.db import models
from django.contrib.postgres.fields import JSONField
# from timezone_field import TimeZoneField
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import transaction
import numpy as np
import cv2

class Myuser(models.Model):
    age = models.BooleanField(blank=True, null=True)
    privacy = models.BooleanField(blank=True, null=True)
    receive_news = models.BooleanField(blank=True, null=True)
    email = models.EmailField(unique=True)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='avtar/', default='avtar/avtar.png')
    csrf_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Myteam(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True)
    team_note = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='team_images/', blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    registration = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    representative = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    items = models.CharField(max_length=10, blank=True, null=True)
    team_mode = models.CharField(max_length=30,blank=True, null=True)
    email = models.ForeignKey(Myuser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Permission(models.Model):
    PERMISSION_TYPES = (
        ('stockin', 'Stockin'),
        ('stockout', 'Stockout'),
        ('adjust', 'Adjust'),
        ('item', 'Item'),
        ('attribute', 'Attribute'),
        ('partner', 'Partner'),
    )
    name = models.CharField(max_length=30, choices=PERMISSION_TYPES, unique=True)

    def __str__(self):
        return self.name
    

class Permiteduser(models.Model):
    PERMISSION_TYPES = (
        ('admin','Admin'),
        ('viewer','Viewer')
    )
    permission = models.CharField(max_length=30, choices=PERMISSION_TYPES, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    email = models.EmailField(unique=True)
    otp_code = models.CharField(max_length=6, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    myteam = models.ForeignKey(Myteam, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('no', 'No'),
        ('yes', 'Yes'),
    )
    permission_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='no')
    additional_permission = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self): 
        return str(self.id)
    
    
class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.JSONField()
    role = models.ForeignKey(Myteam, on_delete=models.CASCADE, null=True, blank=True)            # must change the null=True

    
class CompanyInformation(models.Model):
    company_name = models.CharField(max_length=100)
    business_regd_number = models.CharField(max_length=100)
    address =  models.CharField(max_length=200)
    company_representative = models.CharField(max_length=100)
    phone = models.BigIntegerField(unique=True)
    team = models.ForeignKey(Myuser, on_delete=models.CASCADE)
    

class Item_Information(models.Model):
    Name = models.CharField(max_length=200, blank=True, null=True)
    Barcode = models.CharField(max_length=100, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    initial_quantity = models.BigIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    myteam = models.ForeignKey(Myteam, on_delete=models.CASCADE)
    feature_vector = models.BinaryField(blank=True, null=True)
    def __str__(self): 
        return str(self.id)
    
@receiver(post_save, sender=Item_Information)
def extract_features(sender, instance, **kwargs):
    def process_image():
        if instance.image:
            try:
                image = cv2.imread(instance.image.path)
                if image is None:
                    return None

                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                sift = cv2.SIFT_create()
                _, des = sift.detectAndCompute(gray, None)
                instance.feature_vector = des.tobytes() if des is not None else None
                instance.save(update_fields=['feature_vector'])
            except Exception as e:
                print(f"Error extracting features: {e}")

    transaction.on_commit(process_image)
    

class ItemAttribute(models.Model):
    attribute_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_value = models.CharField(max_length=100, blank=True, null=True)
    attribute_type = models.CharField(max_length=100, blank=True, null=True)
    name = models.ForeignKey(Myteam, on_delete=models.CASCADE)
    item = models.ForeignKey(Item_Information,on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.attribute_name}: {self.attribute_value}"
    
    
    # class Meta:
    #     permissions = [
    #         ("create_attribute", "Can create attribute"),
    #         ("edit_attribute", "Can edit attribute"),
    #         ("delete_attribute", "Can delete attribute"),
    #     ]
    
class Transaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.transaction_id)
    
class Stockin(models.Model):
    supplier = models.CharField(max_length=100)
    initial_quantity = models.BigIntegerField()
    present_quantity = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=False)
    memo = models.TextField(max_length=500, blank=True, null=True)
    rack_no = models.CharField(blank=True, null=True)
    myteam = models.ForeignKey(Item_Information, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='stockins')
    def __str__(self): 
        return str(self.id)

class Stockout(models.Model):
    customer = models.CharField(max_length=100)
    initial_quantity = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=False)
    memo = models.TextField(max_length=500, blank=True, null=True)
    rack_no = models.CharField(blank=True, null=True)
    myteam = models.ForeignKey(Item_Information, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='stockouts')
    def __str__(self): 
        return str(self.id)
    
    # class Meta:
    #     permissions = [
    #         ("create_stockout", "Can create stock out"),
    #     ]
    
class Adjust(models.Model):
    memo = models.TextField(max_length=500, blank=True, null=True)
    initial_quantity = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    rack_no = models.CharField(blank=True, null=True)
    myteam = models.ForeignKey(Item_Information, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='adjusts')
    def __str__(self):
        return str(self.id)
    
    # class Meta:
    #     permissions = [
    #         ("create_adjust", "Can create adjust"),
    #     ]
       
    
class Supplier(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    memo = models.TextField(max_length=500)
    favorite = models.BooleanField(blank=True, null=True)
    foreign = models.ForeignKey(Myteam, on_delete=models.CASCADE)
    def __str__(self): 
        return str(self.mobile)
    
class Customer(models.Model):
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    mobile = models.BigIntegerField(unique=True)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    memo = models.TextField(max_length=500)
    favorite = models.BooleanField(blank=True, null=True)
    foreign = models.ForeignKey(Myteam, on_delete=models.CASCADE)
    def __str__(self): 
        return str(self.mobile)
    
    

    
    
# attribute = models.JSONField(default=dict, blank=True,null=True)

# class Stockin(models.Model):
#     supplier = models.CharField(max_length=100)
#     Name = models.CharField(max_length=200)
#     Barcode = models.CharField(max_length=100)
#     cost = models.DecimalField(max_digits=10, decimal_places=2)
#     Price = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(blank=True, null=True)
#     initial_quantity = models.BigIntegerField()
#     created_at = models.DateTimeField(auto_now_add=False)
#     memo = models.TextField(max_length=500)
#     myteam = models.ForeignKey(Item_Information, on_delete=models.CASCADE)
#     def __str__(self): 
#         return str(self.Name)