from django.shortcuts import render
from configuration.models import UserStatusConfig, QuizConfig
from configuration.api.serializers import UserStatusConfigSerializer, QuizConfigSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class UserStatusConfigList(APIView):
    def get(self, request):
        lists = UserStatusConfig.objects.all()
        serializer = UserStatusConfigSerializer(lists, many=True)
        return Response(serializer.data)

class UserStatusConfigDetail(APIView):
    def get(self, request, pk):
        try:
            user_status_config_query = UserStatusConfig.objects.get(pk=pk)
            serializer = UserStatusConfigSerializer(user_status_config_query, many=False)
            return Response(serializer.data, status=200)
        except UserStatusConfig.DoesNotExist:
            return Response(status=404)


    def post(self, request):
        serializer = UserStatusConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def put(self, request, pk):
        try:
            user_status_config_query = UserStatusConfig.objects.get(pk=pk)
            serializer = UserStatusConfigSerializer(user_status_config_query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except UserStatusConfig.DoesNotExist:
            return Response(status=404)


    def delete(self, request, pk):
        try:
            user_status_config_query = UserStatusConfig.objects.get(pk=pk)
            user_status_config_query.delete()
            return Response(status=204)
        except UserStatusConfig.DoesNotExist:
            return Response(status=404)


class QuizConfigList(APIView):
    def get(self, request):
        lists = QuizConfig.objects.all()
        serializer = QuizConfigSerializer(lists, many=True)
        return Response(serializer.data)


class QuizConfigDetail(APIView):
    def get(self, request, pk):
        try:
            quiz_config_query = QuizConfig.objects.get(pk=pk)
            serializer = QuizConfigSerializer(quiz_config_query, many = False)
            return Response(serializer.data, status=200)
        except QuizConfig.DoesNotExist:
            return Response(status=404)


    def post(self, request):
        serializer = QuizConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def put(self, request, pk):
        try:
            quiz_config_query = QuizConfig.objects.get(pk=pk)
            serializer = QuizConfigSerializer(quiz_config_query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except QuizConfig.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            quiz_config_history = QuizConfig.objects.get(pk=pk)
            quiz_config_history.delete()
            return Response(status=204)
        except QuizConfig.DoesNotExist:
            return Response(status=404)