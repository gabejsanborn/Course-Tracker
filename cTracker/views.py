from django.shortcuts import render, redirect

from .models import Student, Course, Enrolled
from .forms import CourseForm, EnrolledForm


# Create your views here.
def home(request):
    """ the homepage of the main app """
    return render(request, 'main/index.html') # we need to create a file index.html


def courses(request):

    student_id = 1
    student = Student.objects.get(id=student_id)

    enrolleds = student.enrolled_set.all()

    classes= []
    for ele in enrolleds:
        course_id = ele.get_courseID()
        course = Course.objects.get(name=course_id)
        courseName = course.get_coursename()
        courseCode = course.get_coursecode()
        grade = ele.get_grade()
        semester = ele.get_semester()

        classinfo = ClassInfo(courseName, courseCode, grade, semester)

        classes.append(classinfo)

    context = {'enrolled': enrolleds, 'classes': classes}
    return render(request, 'main/courses.html', context)


def addcourse(request):

    if request.method != 'POST':
        form = CourseForm()

    else:
        form = CourseForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect('cTracker:courses')

    context = {'form': form}
    return render(request, 'main/new_course.html', context)


def enroll(request):

    if request.method != 'POST':
        form = EnrolledForm()

    else:
        form = EnrolledForm(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect('cTracker:courses')

    context = {'form': form}
    return render(request, 'main/course_enroll.html', context)


def login(request):
    return render(request, 'main/login.html')




class ClassInfo:

    def __init__(self, name, code, grade, semester):
        self.name = name
        self.code = code
        self.grade = grade
        self.semester = semester

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def get_grade(self):
        return self.grade

    def get_semester(self):
        return self.semester

