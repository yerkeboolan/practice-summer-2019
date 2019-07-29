from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from subjectContent.models import Video, Test, Question, Answer
from subjectContent.api.serializers import VideoSerializer, TestSerializer, QuestionSerializer, AnswerSerializer

# Create your views here.

class VideoList(APIView):
    def get(self, request):
        lists = Video.objects.all()
        serializer = VideoSerializer(lists, many = True)
        return Response(serializer.data)

class VideoDetail(APIView):
    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            video_query = Video.objects.get(pk=pk)
            serializer = VideoSerializer(video_query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Video.DoesNotExist:
            return Response(status=404)


    def delete(self, request, pk):
        try:
            video_query = Video.objects.get(pk=pk)
            video_query.delete()
            return Response(status=204)
        except Video.DoesNotExist:
            return Response(status=404)


class TestList(APIView):
    def get(self, request):
        lists = Test.objects.all()
        serializer = TestSerializer(lists, many=True)
        return Response(serializer.data)

class TestDetail(APIView):
    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            test_query = Test.objects.get(pk=pk)
            serializer = TestSerializer(test_query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Test.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            test_query = Test.objects.get(pk=pk)
            test_query.delete()
            return Response(status=204)
        except Test.DoesNotExist:
            return Response(status=404)


class QuestionList(APIView):
    def get(self, request, test_pk):
        lists = Question.objects.filter(test__pk=test_pk)
        serializer = QuestionSerializer(lists, many=True)
        return Response(serializer.data, status=200)


class QuestionDetail(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, question_pk):
        try:
            question_query = Question.objects.get(pk=question_pk)
            serializer = QuestionSerializer(question_query, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Question.DoesNotExist:
            return Response(status=404)
