from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, user_name, password, **extra_fields):
        if not user_name:
            raise ValueError('The User Name field must be set')
        user = self.model(user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')

        return self.create_user(user_name, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    status_choice = (
        ('A', 'Active'),
        ('D', 'Deactivated')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20, blank=False, null=False)
    father_name = models.CharField(max_length=20, blank=False, null=False)
    grand_father_name = models.CharField(max_length=20, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    region = models.CharField(max_length=20, blank=False, null=False)
    city = models.CharField(max_length=20, blank=False, null=False)
    religion = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    emergency_name = models.CharField(max_length=20, blank=False, null=False)
    emergency_phone = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    user_name = models.CharField(max_length=20, blank=False, null=False, unique=True)
    created_by = models.CharField(max_length=20, blank=False, null=False)
    status = models.CharField(max_length=1, choices=status_choice)
    type_of_account = models.CharField(max_length=20, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['name', 'father_name', 'grand_father_name', 'date_of_birth', 'region', 'city', 'religion', 'phone_number', 'emergency_name', 'emergency_phone', 'created_by', 'status', 'type_of_account']

    objects = UserManager()

    def __str__(self):
        return self.user_name
    def has_perm(self,perm,obj=None):
        return self.is_superuser
    def has_module_perms(self,perm,obj=None):
        return self.is_superuser


	
	

