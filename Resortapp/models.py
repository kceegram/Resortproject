from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
from django.conf import settings

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    


class User(AbstractBaseUser, PermissionsMixin):
        
        groups = models.ManyToManyField(
        'auth.Group',
        related_name='resortapp_user_groups',  # unique related_name for groups
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

        user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='resortapp_user_permissions',  # unique related_name for user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

        auto_id = models.PositiveBigIntegerField(unique=False, null=True, blank=True)
        email = models.EmailField(max_length=255, unique=True)
        name = models.CharField(max_length=255, null=True, blank=True)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)
        date_joined = models.DateTimeField(auto_now_add=True)
        last_login = models.DateTimeField(null=True, blank=True)
        profile_pic = models.ImageField(default='default.png', blank=True, null=True, upload_to='profile_pics/')

        objects = CustomUserManager()

        USERNAME_FIELD = 'email'
        EMAIL_FIELD = 'email'
        REQUIRED_FIELDS = []

        class Meta:
            verbose_name = 'user permissions'
            verbose_name_plural = 'users'

        def get_full_name(self):
            return self.name

        def get_short_name(self):
            return self.name

        def save(self, *args, **kwargs):
            count_id = User.objects.all().count()
            self.auto_id = count_id+1
            super(User, self).save(*args, **kwargs)

        def _str_(self):
            return self.name
        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)     
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(max_length=255, blank=True, null=True)
    profile_pic = models.ImageField(default='default.png', blank=True, null=True, upload_to='profile_pics/')


    def __str__(self):
        return (self.user.name)
    

class RoomCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
          return self.name
    


class Room(models.Model):
    category = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='room_pics/')
    description = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
    


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    room = models.ForeignKey(RoomCategory, on_delete=models.CASCADE, blank=True, null=True)
    booked_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    pay_status = models.BooleanField(default=False, blank=True, null=True)


    def __str__(self):
        return f"This {self.room.name} is booked"
    

