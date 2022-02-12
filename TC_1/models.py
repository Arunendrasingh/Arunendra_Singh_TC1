from datetime import datetime
from email import message
from pyexpat import model
from django.db import models

# Create your models here.
class Contact_Info(models.Model):
    Name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    is_solved = models.BooleanField(default=False)
    solved_by = models.CharField(max_length=50)
    datetime = models.DateTimeField(auto_now_add=True)
    issue_date = models.DateTimeField(auto_now_add=True)
    solving_date = models.DateTimeField(null=True)

class City(models.Model):
    name = models.CharField(max_length=70)


class State(models.Model):
    name = models.CharField(max_length=70)


class Address_info(models.Model):
    city_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    street = models.TextField()
    zip_code = models.IntegerField()
    user_email = models.EmailField()

