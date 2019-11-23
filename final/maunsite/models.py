from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	SiteName=models.CharField(max_length=200)
	UVI=models.CharField(max_length=200)
	PublishAgency=models.CharField(max_length=200)
	WGS84Lon=models.CharField(max_length=200)
	County=models.CharField(max_length=200)
	WGS84Lat=models.CharField(max_length=200)
	PublishTime=models.CharField(max_length=200)

def __str__(self):
		return "{}-{}".format(self.sitename)

