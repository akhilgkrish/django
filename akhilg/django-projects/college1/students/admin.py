from django.contrib import admin
from . models import *

# Register your models here.


class Department_display(admin.ModelAdmin):
    list_display=['name']
class Teacher_display(admin.ModelAdmin):
    list_display=['name','department']
class Batch_display(admin.ModelAdmin):
    list_display=['batch']
class Student_display(admin.ModelAdmin):
    list_display=['name','batch','teacher']


admin.site.register(Department,Department_display)
admin.site.register(Teacher,Teacher_display)
admin.site.register(Batch,Batch_display)
admin.site.register(Students,Student_display)