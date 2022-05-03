from django import forms
from .models import Course, Student, Enrolled


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'courseCode']
        labels = {'name': 'Course Name', 'courseCode': 'Course Code'}


class EnrolledForm(forms.ModelForm):
    class Meta:
        model = Enrolled
        fields = ['student', 'course', 'semester', 'grade']
        labels = {'student': 'Student ID', 'course': 'Course ID', 'semester': 'Semester', 'grade': 'Grade'}