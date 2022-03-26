from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class players_list(models.Model):
    TYPE_CHOICES = (
    ('mod', 'Author'),
    ('pla', 'Player'),
    )
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, unique=True, null=True, blank=True, default=None)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=8)

    def __str__(self):
        return str(self.pk)+' '+ self.username+'  '+self.email


class Challenges(models.Model):
    c_name = models.CharField(max_length=100)
    c_category = models.CharField(max_length=50)
    c_description = models.CharField(max_length=1000)
    c_point = models.IntegerField()
    c_flag = models.CharField(max_length=350)

    def __str__(self):
        return str(self.pk)+" "+ self.c_name+ " " + self.c_category


class score(models.Model):
    solver_name = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    solved = models.ForeignKey(Challenges, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(auto_now=False)
    points = models.IntegerField(null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(default='null', max_length=30)
    def __str__(self):
        return f'{self.user.username} Profile'


class Notify(models.Model):
    info = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now=True)

class Rules(models.Model):
    details = models.CharField(max_length=10000)
    time = models.DateTimeField(auto_now=True)