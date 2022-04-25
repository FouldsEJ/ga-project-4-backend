from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField



# Create your models here.

ABILITY_CHOICES = (
    ('beginner','BEGINNER'),
    ('intermediate', 'INTERMEDIATE'),
    ('advanced','ADVANCED'),
    ('world class','WORLD CLASS'),
)

GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('non-binary', 'NON-BINARY'),
    ('transgender', 'TRANSGENDER'),
    ('i prefer not to say', 'I PREFER NOT TO SAY')
)

class CustomUser(AbstractUser):
  image = models.CharField(max_length=200, blank=True)
  description = models.TextField(max_length=300, blank=True)
  ability = models.CharField(max_length=12, choices=ABILITY_CHOICES, blank=False)
  age = models.IntegerField(blank=False, null=True)
  gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=False)
  birthday = models.DateField(blank=True, null=True)
  town = models.CharField(max_length=50, blank=True)
  country = CountryField(blank_label='(select country)', blank=False)
  lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
  long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
