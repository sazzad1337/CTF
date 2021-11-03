from django.db import models

# Create your models here.
class players_list(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=8)

    def __str__(self):
        return str(self.pk)+' '+ self.username+'  '+self.email


class scoreboard(models.Model):
    username = models.CharField(max_length=20)
    score = models.IntegerField()
    password = models.CharField(max_length=8)