from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

#  Custom User Manager


class UserManager(BaseUserManager):
    
    def create_user(self, email, firstname, lastname, password=None, password2=None):
        """
        Creates and saves a User with the given email, name, tc and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname = lastname
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, lastname,password=None):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            password=password,
            firstname=firstname,
            lastname = lastname
        )
        
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

#  Custom User Model


class User(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        (1, 'public'),
        (2, 'volunteer'),
        (3, 'supervisor'),
        (4, 'engineeer'),
        (5, 'admin'),
    )
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    
    
    
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default = 1)
    firstname = models.CharField(max_length=25, verbose_name='First Name')
    middlename = models.CharField(max_length=25,blank=True,null= True, verbose_name='Middle Name')
    lastname = models.CharField(max_length=25, verbose_name='Last Name')
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
