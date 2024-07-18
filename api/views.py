
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from student.models import Student
from .serializers import StudentSerializer
from classes.models import Class
from .serializers import ClassesSerializer
from classPeriod.models import ClassPeriod
from .serializers import ClassPeriodSerializer
from course.models import Course
from .serializers import CoursesSerializer
from teacher.models import Teacher
from .serializers import TeacherSerializer

class StudentListViews(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)


class ClassListViews(APIView):
    def get(self,request):
        Classes = Class.objects.all()
        serializer = ClassesSerializer(Classes,many=True)
        return Response(serializer.data)
    
class ClassPeriodListViews(APIView):
    def get(self,request):
        Periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(Periods,many=True)
        return Response(serializer.data)
    
class CoursesListViews(APIView):
    def get(self,request):
        Periods = Course.objects.all()
        serializer = CoursesSerializer(Periods,many=True)
        return Response(serializer.data)
    
class TeacherListViews(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)