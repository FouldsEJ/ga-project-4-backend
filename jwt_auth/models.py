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
    ('female', 'FEMALE')
)

class CustomUser(AbstractUser):
  image = models.CharField(max_length=200)
  description = models.TextField(max_length=300)
  ability = models.CharField(max_length=12, choices=ABILITY_CHOICES)
  # age = models.IntegerField(blank=True, null=True)
  gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
  town = models.CharField(max_length=50)
  country = CountryField(blank_label='(select country)')
  # lat = models.DecimalField(max_digits=9, decimal_places=6)
  # long = models.DecimalField(max_digits=9, decimal_places=6)
