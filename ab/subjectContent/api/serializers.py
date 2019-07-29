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

        read_only_fields = ('pk',)


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

        read_only_fields = ('pk', )

    def validate(self, data):
        error_msg_two_answer = "There will be at least two options"
        error_msg_right_answer = "There will be one right answer"

        if data:
            if data['ans_question']:
                if len(data['ans_question']) < 2:
                    raise serializers.ValidationError(error_msg_two_answer)

                true_ans = 0
                for answer_data in data['ans_question']:
                    if answer_data['flag']:
                        true_ans += 1
                if true_ans > 1 or true_ans == 0:
                    raise serializers.ValidationError(error_msg_right_answer)
            else:
                raise serializers.ValidationError(error_msg_two_answer)
        return data

    def create(self, validated_data):
        answers = validated_data.pop('ans_question')
        question_data = self.create_question(**validated_data)
        self.create_answers(question_data, answers)
        return question_data

    def update(self, instance, validated_data):
        answer = Answer.objects.filter(question=instance)
        answer.delete()
        try:
            question = Question.objects.get(pk=instance.pk)
            question.question = validated_data.pop('question')
            question.save()
            self.create_answers(question, validated_data.pop('ans_question'))
            return question
        except Question.DoesNotExist:
            raise serializers.ValidationError("question not found")
        return instance

    def create_question(self, **variables):
        question_data = Question.objects.create(**variables)
        return question_data

    def create_answers(self, question_data, answers_data):
        for answer_data in answers_data:
            Answer.objects.create(question=question_data, **answer_data)


class TestSerializer(serializers.ModelSerializer):
    q_test = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ('pk', 'subtopic', 'q_test', )

        read_only_fields = ('pk',)


