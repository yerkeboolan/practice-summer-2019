from rest_framework import serializers
from subject.models import Subject, Subtopic, Topic

class SubjectSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(required=True)

    class Meta:
        model = Subject
        fields = ('pk',
                  'title')
        read_only_fields = ('pk',)

class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)

class SubjectTopicSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = (
            'pk',
            'title',
            'topic')


class SubtopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)

class TopicSubtopicSerializer(serializers.ModelSerializer):
    subtopic = SubtopicSerializer(many=True, read_only=True)
    class Meta:
        model = Topic
        fields = (
            'pk',
            'title',
            'is_quiz',
            'subject',
            'subtopic'
        )
        read_only_fields = ('pk',)

class SubjectTopicSubtopicSerializer(serializers.ModelSerializer):
    topic = TopicSubtopicSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = (
            'pk',
            'title',
            'topic',
        )
