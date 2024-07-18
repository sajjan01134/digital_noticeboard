from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    ROLES = (
        ('super_admin', 'Super Admin'),
        ('admin', ' Admin'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=15, choices=ROLES,blank=True, null=True)
    username = models.CharField(max_length=150, unique=True,db_index=True) # Ensure username is indexed

def is_dnb_or_superuser(self):
    return self.is_superuser or self.role == 'super_admin'
# Create your models here.
