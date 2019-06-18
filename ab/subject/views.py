from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from subject.models import Subject, Topic, Subtopic
from subject.api.serializers import SubjectSerializer, SubtopicSerializer, TopicSerializer


#Create your views here.


@api_view(['GET'])
def subject_list(request):
    if request.method == 'GET':
        lists = Subject.objects.all()
        serializer = SubjectSerializer(lists, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def topic_list(request):
    if request.method == 'GET':
        lists = Topic.objects.all()
        serializer = TopicSerializer(lists, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def subtopic_list(request):
    if request.method == 'GET':
        lists = Subtopic.objects.all()
        serializer = SubtopicSerializer(lists, many=True)
        return Response(serializer.data)
