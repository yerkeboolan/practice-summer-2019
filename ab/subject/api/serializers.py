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


class SubtopicSerializer(serializers.ModelSerializer):
    # topic = serializers.IntegerField(write_only=True)
    class Meta:
        model = Subtopic
        fields = (
            'pk',
            'title',
            'topic'
        )
        read_only_fields = ('pk', )


    # def to_representation(self, instance):
    #     data = super(SubtopicSerializer, self).to_representation(instance)
    #     if instance.topic:
    #         data['topic_detail'] = {
    #             'pk': instance.topic.pk,
    #             'title': instance.topic.title,
    #             'bul_quiz_ba': instance.topic.is_quiz
    #         }
    #     return data

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


    # def to_representation(self, instance):
    #     data = super(TopicSubtopicSerializer, self).to_representation(instance)
    #     if instance.subject:
    #         data['subject_detail'] = {
    #             'title': instance.subject.title,
    #         }
    #     return data

class SubjectTopicSubtopicSerializer(serializers.ModelSerializer):
    topic = TopicSubtopicSerializer(many=True, read_only=True)
    class Meta:
        model = Subject
        fields = (
            'pk',
            'title',
            'topic',
        )


