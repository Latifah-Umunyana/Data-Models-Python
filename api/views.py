
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
from rest_framework import status

class StudentListViews(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class StudentDetailView(APIView):
    def get(self,request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request, id):
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class ClassListViews(APIView):
    def get(self,request):
        Classes = Class.objects.all()
        serializer = ClassesSerializer(Classes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class ClassDetailView(APIView):
    def get(self,request, id):
        classe = Class.objects.get(id=id)
        serializer = ClassesSerializer(classe)
        return Response(serializer.data)
    
    def put(self,request, id):
        classe = Class.objects.get(id=id)
        serializer = ClassesSerializer(classe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        classe = Class.objects.get(id=id)
        classe.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class ClassPeriodListViews(APIView):
    def get(self,request):
        Periods = ClassPeriod.objects.all()
        serializer = ClassPeriodSerializer(Periods,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ClassPeriodSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class ClassPeriodDetailView(APIView):
    def get(self,request, id):
        classe = Class.objects.get(id=id)
        serializer = ClassPeriodSerializer(classe)
        return Response(serializer.data)
    
    def put(self,request, id):
        period = ClassPeriod.objects.get(id=id)
        serializer = ClassPeriodSerializer(period, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        classe = Class.objects.get(id=id)
        classe.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

class CoursesListViews(APIView):
    def get(self,request):
        Periods = Course.objects.all()
        serializer = CoursesSerializer(Periods,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class CoursesDetailView(APIView):
    def get(self,request, id):
        course = Course.objects.get(id=id)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)
    
    def put(self,request, id):
        course = Course.objects.get(id=id)
        serializer = CoursesSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
class TeacherListViews(APIView):
    def get(self,request):
        Teachers = Teacher.objects.all()
        serializer = TeacherSerializer(Teachers, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = TeacherSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
class TeacherDetailView(APIView):
    def get(self,request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self,request, id):
        teacher = Teacher.objects.get(id=id)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request, id):
        teacher = Teacher.objects.get(id=id)
        teacher.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    
