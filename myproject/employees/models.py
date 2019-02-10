from django.db import models


# Create Category Model
class Category(models.Model):
	category_name = models.CharField(max_length=50, null=False)
	salary = models.FloatField(blank=True)

	def __str__(self):
		return self.category_name


# Create Employee Model
class Employee(models.Model):
	name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=20)
	civil_status = models.CharField(max_length=20)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d')
	degree = models.CharField(max_length=30)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	bio = models.TextField(max_length=200)
	birth = models.DateTimeField(blank=True)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name + ' ' + self.last_name


# Create Document Model
class Document(models.Model):
	doc_number = models.IntegerField(blank=True, null=False)
	doc_name = models.CharField(max_length=20)
	doc_date = models.DateField(blank=False)
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

	def __str__(self):
		return self.employee.last_name + ' - ' + self.doc_name


class Attachment(models.Model):
	att_file = models.FileField('files/%Y/%m/%d')
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	document = models.ForeignKey(Document, on_delete=models.CASCADE)

	def __str__(self):
		return self.employee.last_name + ' - ' + self.document.doc_name

