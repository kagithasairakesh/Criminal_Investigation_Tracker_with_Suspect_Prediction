from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
	admin_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=30)
	image = models.ImageField(upload_to="images/admin/", blank=True)
	phone_number = models.CharField(max_length=12)
	mail = models.EmailField(max_length=50)
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)

	def __str__(self):
		return str(self.name)

class Officer(models.Model):
	officer_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=40)
	image = models.ImageField(upload_to="images/officer/")
	department = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=12)
	mail = models.EmailField(max_length=50)
	rank_of_officer = models.CharField(max_length=30)
	location = models.CharField(max_length=20)
	created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="admin_officers")
	user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name="user_officer")

	def __str__(self):
		return str(self.name)