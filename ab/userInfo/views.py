from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student, Teacher
from userInfo.api.serializers import StudentSerializerInfo, StudentStatusSerializer, StudentGroupSerializerInfo
from configuration.models import UserStatusConfig
from rest_framework.response import Response

# Create your views here.


class StudentListFullInfo(APIView):
    def get(self, request):
        lists = Student.objects.all()
        serializer = StudentSerializerInfo(lists, many=True)
        return Response(serializer.data)


class StudentDetailFullInfo(APIView):
    def get(self, request, pk):
        try:
            student_query = Student.objects.get(pk=pk)
            serializer = StudentSerializerInfo(student_query, many=False)
            return Response(serializer.data, status=200)
        except Student.DoesNotExist:
            return Response(status=404)

class StudentDetail(APIView):
    def put(self, request, pk):
        try:
            student_query = Student.objects.get(pk=pk)
            serializer = StudentStatusSerializer(data=request.data)
            if serializer.is_valid():
                try:
                    userStatusConfig = UserStatusConfig.objects.get(pk=serializer.data['status'])
                    student_query.status = userStatusConfig
                    student_query.info.is_active = userStatusConfig.is_active
                    student_query.save()
                    student_serializer = StudentSerializerInfo(student_query, many=False)
                    return Response(student_serializer.data, status=201)
                except UserStatusConfig.DoesNotExist:
                    return Response(status=404)
            return Response(serializer.errors, status=400)
        except Student.DoesNotExist:
            return Response(status=404)

class StudentGroupFullInfo(APIView):
    def get(self, request, student_pk):
        try:
            student_query = Student.objects.get(pk=student_pk)
            serializer = StudentGroupSerializerInfo(student_query, many=False)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=404)