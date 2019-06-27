from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student, Teacher
from userInfo.api.serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.


class StudentListFullInfo(APIView):
    def get(self, request):
        lists = Student.objects.all()
        serializer = StudentSerializer(lists, many=True)
        return Response(serializer.data)


class StudentDetailFullInfo(APIView):
    def get(self, request, pk):
        try:
            student_query = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student_query, many=False)
            return Response(serializer.data, status=200)
        except Student.DoesNotExist:
            return Response(status=404)
