from django.db import models


# Create Category Model
class Category(models.Model):
	cat_name = models.CharField(max_length=50)
	cat_salary = models.FloatField(blank=True)

	def __str__(self):
		return self.cat_name


class Department(models.Model):
	dep_acronym = models.CharField(max_length=10)
	dep_name = models.CharField(max_length=50)
	dep_address = models.CharField(max_length=50, blank=True)
	dep_email = models.EmailField(max_length=50, blank=True)
	dep_phone = models.IntegerField(blank=True)

	def __str__(self):
		return self.dep_acronym + ' - ' + self.dep_name


# Create Employee Model
class Employee(models.Model):
	cod = models.IntegerField()
	name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=20)
	civil_status = models.CharField(max_length=20, blank=True)
	photo = models.ImageField(upload_to='photos', blank=True)
	degree = models.CharField(max_length=30, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	department = models.ForeignKey(Department, on_delete=models.CASCADE)
	bio = models.TextField(max_length=200, blank=True)
	birth = models.DateTimeField(blank=True)
	address = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	city = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' ' + self.last_name


# Create Document Model
class Document(models.Model):
	doc_number = models.IntegerField()
	doc_name = models.CharField(max_length=20)
	doc_date = models.DateField(auto_now_add=True)
	doc_file = models.FileField(upload_to='files', blank=True)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

	def __str__(self):
		return self.employee.last_name + ' - ' + self.doc_name
