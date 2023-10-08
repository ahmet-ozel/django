from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User

class Company(models.Model):
    companyID = models.IntegerField(primary_key=True, null=False)
    companyName = models.CharField(max_length=100, null=False)
    subscriptionDate = models.DateField(null=True, blank=True)
    lastlogin_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    # Mevcut User model alanlarını eklemek için kullanabilirsiniz
    api = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=20, null=True)
    companyID = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
    
class Person(models.Model):
    person_tc = models.CharField(max_length=11, primary_key=True)
    person_name = models.CharField(max_length=50, null=True, blank=True)
    person_lastname = models.CharField(max_length=50, null=True, blank=True)
    university = models.CharField(max_length=255, null=True, blank=True)


class Meeting(models.Model):
    meeting_id = models.IntegerField(primary_key=True)
    companyID = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, db_column='companyID')
    userid = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, db_column='userid')  # CustomUser modelini kullanıyoruz
    person_tc = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, db_column='person_tc')  # Person modeline olan ilişki
    person_name = models.CharField(max_length=50, null=True, blank=True)
    meeting_date = models.DateField(null=True, blank=True)

class MeetingDescription(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True)
    meeting_date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    gender = models.CharField(max_length=6, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    emotion = models.CharField(max_length=10, null=True, blank=True)
    precisions = models.FloatField(null=True, blank=True)

class SpeakingDescription(models.Model):
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    speaker = models.CharField(max_length=255, null=True, blank=True)

