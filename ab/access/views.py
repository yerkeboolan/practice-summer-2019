from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from access.models import VideoAccess, TestAccess
from access.api.serializers import VideoAccessSerializer, TestAccessSerializer
from rest_framework import status

# Create your views here.


class VideoAccessDetail(APIView):
    def post(self, request):
        serializer = VideoAccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


    def put(self, request, pk):
        try:
            access_query = VideoAccess.objects.get(pk=pk)
            serializer = VideoAccessSerializer(access_query, data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except VideoAccess.DoesNotExist:
            return Response(status=404)


class TestAccessDetail(APIView):
    def post(self, request):
        serializer = TestAccessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)