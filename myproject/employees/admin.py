from django.contrib import admin
from .models import Employee, Category, Document, Attachment


# Register your models here.
admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Document)
admin.site.register(Attachment)
