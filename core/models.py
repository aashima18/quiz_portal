from django.db import models
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import RegexValidator



class User(AbstractUser):
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254,unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=10)


class Question(models.Model):
    questions = models.CharField(max_length = 200)
    choice_one = models.CharField(max_length = 200)
    choice_two = models.CharField(max_length = 200)
    choice_three = models.CharField(max_length = 200)
    choice_four = models.CharField(max_length = 200)
    choice_five = models.CharField(max_length = 200)
    answer = models.CharField(max_length = 200)

    def __str__(self):
        return self.questions

class Score(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    score = models.CharField(max_length = 200)