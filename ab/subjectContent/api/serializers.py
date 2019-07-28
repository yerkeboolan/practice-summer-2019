from rest_framework import serializers
from subjectContent.models import Video, Test, Question, Answer


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'pk',
            'url',
            'subtopic'
        )
        read_only_fields = ('pk', )

    def to_representation(self, instance):
        data = super(VideoSerializer, self).to_representation(instance)
        if instance.subtopic:
            data['subtopic_detail'] = {
                'pk': instance.subtopic.pk,
                'title': instance.subtopic.title,
            }
        return data



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'answer', 'flag', )

        read_only_fields = ('pk', )


    #
    # def validate(self, data):
    #     true_ans = 0
    #     if data:
    #         if data['answer']:
    #             if data['flag']:


class QuestionSerializer(serializers.ModelSerializer):
    ans_question = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ('pk', 'question', 'test', 'ans_question', )

        read_only_fields = ('pk',)



    def create(self, validated_data):
        answers_data = validated_data.pop('ans_question')
        true_ans = 0
        for answer_data in answers_data:
            if answer_data['flag']:
                true_ans += 1
        if true_ans > 1 or true_ans == 0:
            raise serializers.ValidationError('There will be at least one right answer')
        question_data = Question.objects.create(**validated_data)
        if len(answers_data) < 2:
            raise serializers.ValidationError('There will be at least two options')
        for answer_data in answers_data:
            Answer.objects.create(question=question_data, **answer_data)
        return question_data


class TestSerializer(serializers.ModelSerializer):
    q_test = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('pk', 'subtopic', 'q_test', )

        read_only_fields = ('pk',)


