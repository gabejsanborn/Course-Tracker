from django.db import models


# Create your models here.
class Course(models.Model):
    """A class that describes a course"""
    name = models.CharField(max_length=50)
    courseCode = models.CharField(max_length=10)

    def __str__(self):
        """Method to determine what is written when object is printed"""

        string = self.name
        return string

    def get_coursecode(self):
        return self.courseCode

    def get_coursename(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        """Method to display name"""
        return self.name


class Enrolled(models.Model):
    """A class that describes an enrolled course"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    grade = models.FloatField()

    def __str__(self):
        """Method to determine what is written when object is printed"""
        return "enrolled in course"

    def get_grade(self):
        return self.grade

    def get_semester(self):
        return self.semester

    def get_courseID(self):
        return self.course



