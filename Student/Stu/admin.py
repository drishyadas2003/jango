from django.contrib import admin
from.models import *

# Register your models here.
class Teacher_dispaly(admin.ModelAdmin):
    list_display=['teacher']


class Batch_dispaly(admin.ModelAdmin):
    list_display=['batch']
    
class Student_dispaly(admin.ModelAdmin):
    list_display=['name','age','contact','batch','teacher']
    
    
admin.site.register(Teacher,Teacher_dispaly)
admin.site.register(Batch,Batch_dispaly)
admin.site.register(Student,Student_dispaly)
