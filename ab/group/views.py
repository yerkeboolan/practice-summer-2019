from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from group.models import GroupStudent, Group
from group.api.serializers import GroupSerializer, GroupStudentSerializer
from rest_framework.views import APIView

# Create your views here.

class GroupList(APIView):
    def get(self, request):
        lists = Group.objects.all()
        serializer = GroupSerializer(lists, many=True)
        return Response(serializer.data)

class GroupDetail(APIView):
    def get(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            serializer = GroupSerializer(group, many=False)
            return Response(serializer.data, status=200)
        except Group.DoesNotExist:
            return Response(status=404)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)

    def put(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            serializer = GroupSerializer(group, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=500)
        except Group.DoesNotExist:
            return Response(serializer.errors, status=404)

    def delete(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            group.delete()
            return Response(status=204)
        except Group.DoesNotExist:
            return Response(status=404)

class GroupStudentList(APIView):
    def get(self, request):
        lists = GroupStudent.objects.all()
        serializer = GroupStudentSerializer(lists, many=True)
        return Response(serializer.data)

class GroupStudentDetail(APIView):
    def get(self, request, pk):
        try:
            groupStudent = GroupStudent.objects.get(pk=pk)
            serializer = GroupStudentSerializer(groupStudent, many=False)
            return Response(serializer.data, status=200)
        except GroupStudent.DoesNotExist:
            return Response(status=404)


    def post(self, request):
        serializer = GroupStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=500)

    def put(self, request, pk):
        try:
            groupStudent = GroupStudent.objects.get(pk=pk)
            serializer = GroupStudentSerializer(groupStudent, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=500)
        except GroupStudent.DoesNotExist:
            return Response(serializer.errors, status=404)


    def delete(self, request, pk):
        try:
            groupStudent = GroupStudent.objects.get(pk=pk)
            groupStudent.delete()
            return Response(status=204)
        except GroupStudent.DoesNotExist:
            return Response(status=404)

