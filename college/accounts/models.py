from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinLengthValidator, MinValueValidator , EmailValidator
from django.core import validators


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_student = False
        user.save(using=self._db)
        return user



     

class User(AbstractBaseUser):
    id = models.BigAutoField(
        primary_key=True
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name',
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name',
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='Email ID',
        validators=[
            validators.EmailValidator('invalid Email')
        ]
 
    )
    date_join=models.DateTimeField(
        auto_now_add=True
    )

    last_update = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Last Login'
    )
  
    

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(slef, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

