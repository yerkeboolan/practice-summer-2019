from rest_framework import serializers
from subject.models import Subject, Subtopic, Topic

class SubjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)

class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    subject = SubjectSerializer(read_only=True)

class SubtopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    topic = TopicSerializer(read_only=True)
