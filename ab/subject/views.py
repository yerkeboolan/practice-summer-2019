from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from subject.models import Subject, Topic, Subtopic
from subject.api.serializers import SubjectSerializer, SubtopicSerializer, TopicSerializer, SubjectTopicSerializer, TopicSubtopicSerializer, SubjectTopicSubtopicSerializer
from rest_framework.views import APIView

#Create your views here.


@api_view(['GET'])
def subject_list(request):
    if request.method == 'GET':
        lists = Subject.objects.all()
        serializer = SubjectSerializer(lists, many=True)
        return Response(serializer.data)

@api_view(["GET"])
def subject_topic_view(request):
    subjects_query = Subject.objects.all()
    serializer = SubjectTopicSerializer(subjects_query, many=True)
    # for subject in subjects_query:
    #     for topic in subject.topic.all():
    #         print(subject.title, topic.title)
    # topics_query = Topic.objects.all()
    # for topic in topics_query:
    #     print(topic.title, topic.subject.title)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def topic_subtopic_view(request):
    topics_query = Topic.objects.all()
    serializer = TopicSubtopicSerializer(topics_query, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def general_view(request):
    subjects_query = Subject.objects.all()
    serializer = SubjectTopicSubtopicSerializer(subjects_query, many=True)

    # for subject in subjects_query:
    #     for topic in subject.topic.all():
    #         for subtopic in topic.subtopic.all():
    #             print(subject.title, topic.title, subtopic.title)

    return Response(serializer.data, status=200)

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

class SubjectList(APIView):
    def get(self, request):
        lists = Subject.objects.all()
        serializer = SubjectSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectTopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            subject_query = Subject.objects.get(pk=pk)
            subject_serializer = SubjectTopicSerializer(subject_query, data=request.data, partial=True)
            if subject_serializer.is_valid():
                subject_serializer.save()
                return Response(subject_serializer.data, status=201)
            return Response(subject_serializer.errors, status=400)
        except Subject.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            subject_query = Subject.objects.get(pk=pk)
            subject_query.delete()
            return Response(status=204)
        except Subject.DoesNotExist:
            return Response(status=404)

class TopicList(APIView):
    def get(self, request):
        lists = Topic.objects.all()
        serializer = TopicSubtopicSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TopicSubtopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            topic_query = Topic.objects.get(pk=pk)
            serializer = TopicSubtopicSerializer(topic_query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Topic.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            topic_query = Topic.objects.get(pk=pk)
            topic_query.delete()
            return Response(status=204)
        except Topic.DoesNotExist:
            return Response(status=404)

class SubtopicList(APIView):
    def get(self, request):
        lists = Subtopic.objects.all()
        serializer = SubtopicSerializer(lists, many=True)
        return Response(serializer.data)



class SubtopicDetail(APIView):
    def get(self, request, pk):
        try:
            subtopic = Subtopic.objects.get(pk=pk)
            serializer = SubtopicSerializer(subtopic, many=False)
            return Response(serializer.data, status=200)
        except Subtopic.DoesNotExist:
            return Response(status=404)

    def post(self, request):
        serializer = SubtopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            subtopic_query = Subtopic.objects.get(pk=pk)
            serializer = SubtopicSerializer(subtopic_query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Subtopic.DoesNotExist:
            return Response(status=404)

    def delete(self, request, pk):
        try:
            subtopic_query = Subtopic.objects.get(pk=pk)
            subtopic_query.delete()
            return Response(status=204)
        except Subtopic.DoesNotExist:
            return Response(status=404)

