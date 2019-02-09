from django.db import models


# Create Employee Model


class Employee(models.Model):
	name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=20)

	def __str__(self):
		return self.name + ' ' + self.last_name



