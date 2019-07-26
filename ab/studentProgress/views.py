from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from studentProgress.models import QuizRating, RealTest, GroupAttendance
from studentProgress.api.serializers import QuizSerializer, RealTestSerializer, GroupAttSerializer
from rest_framework.views import APIView

# Create your views here.


class GroupAttendanceList(APIView):
    def get(self, request, group_pk):
        lists = GroupAttendance.objects.filter(group__pk = group_pk)
        serializer = GroupAttSerializer(lists, many=True)
        return Response(serializer.data, status=200)


class GroupAttendanceDetail(APIView):
    def post(self, request):
        serializer = GroupAttSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, group_attendance_pk):
        try:
            group_query = GroupAttendance.objects.get(pk = group_attendance_pk)
            serializer = GroupAttSerializer(group_query, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except GroupAttendance.DoesNotExist:
            return Response(status=404)


class QuizDetail(APIView):
    def get(self, request, pk):
        try:
            quiz = QuizRating.objects.get(pk=pk)
            serializer = QuizSerializer(quiz, many=False)
            return Response(serializer.data, status=200)
        except QuizRating.DoesNotExist:
            return Response(status=404)

    def post(self, request):
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            quiz = QuizRating.objects.get(pk=pk, student__pk = request.data['student'])
            serializer = QuizSerializer(quiz, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except QuizRating.DoesNotExist:
            return Response(status=404)


    def delete(self, request, pk):
        try:
            quiz = QuizRating.objects.get(pk=pk)
            quiz.delete()
            return Response(status=204)
        except QuizRating.DoesNotExist:
            return Response(status=404)


class RealTestDetail(APIView):
    def get(self, request, pk):
        try:
            test = RealTest.objects.get(pk=pk)
            serializer = RealTestSerializer(test, many=False)
            return Response(serializer.data, status=200)
        except RealTest.DoesNotExist:
            return Response(status=404)

    def post(self, request):
        serializer = RealTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            test = RealTest.objects.get(pk=pk, student__pk=request.data['student'])
            serializer = RealTestSerializer(test, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except RealTest.DoesNotExist:
            return Response(status=404)


    def delete(self, request, pk):
        try:
            test = RealTest.objects.get(pk=pk)
            test.delete()
            return Response(status=204)
        except RealTest.DoesNotExist:
            return Response(status=404)