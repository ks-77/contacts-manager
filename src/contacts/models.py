from django.db import models

from common.validators import validate_phone_number


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20, validators=[validate_phone_number])
    email = models.EmailField(max_length=50, unique=True)
