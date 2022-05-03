from django.contrib import admin

# Register your models here.
from .models import Course
admin.site.register(Course)

from .models import Enrolled
admin.site.register(Enrolled)

from .models import Student
admin.site.register(Student)