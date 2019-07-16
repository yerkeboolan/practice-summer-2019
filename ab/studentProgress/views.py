from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from studentProgress.models import QuizRating, RealTest
from studentProgress.api.serializers import QuizSerializer, RealTestSerializer
from rest_framework.views import APIView

# Create your views here.


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