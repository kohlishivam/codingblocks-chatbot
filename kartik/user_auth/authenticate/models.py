from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser

# Create your models here.
class MyUser(models.Model):
	user=models.ForeignKey(User,null=True,unique=True)
	name = CharField(max_length=100, null=True)
	score=models.IntegerField(max_length=100,null=True)
	isRegistered = models.BooleanField(null=False)