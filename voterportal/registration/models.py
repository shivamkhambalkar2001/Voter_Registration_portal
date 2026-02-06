from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.validators import RegexValidator
from datetime import date

import random
import string

def generate_voter_id():
    voter_id = 'V'
    return voter_id + ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))

def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError("Age must be 18 or above.")

class Voter(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    voter_id = models.CharField(max_length=10, unique=True, default=generate_voter_id, editable=False)
    first_name = models.CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-Z]+$', message='First name must contain only alphabets.')])
    last_name = models.CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-Z]+$', message='Last name must contain only alphabets.')])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6, validators=[RegexValidator(regex='^\d{6}$', message='Pincode must be 6 digits.')])
    date_of_birth = models.DateField(validators=[validate_age])
    contact = models.CharField(max_length=10, validators=[RegexValidator(regex='^\d{10}$', message='Contact must be 10 digits.')])

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.voter_id}"
