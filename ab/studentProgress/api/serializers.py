from rest_framework import serializers
from studentProgress.models import QuizRating, RealTest, GroupAttendance, StudentAttendance
from configuration.models import QuizConfig
from group.models import Group, GroupStudent
from subject.models import Topic
from rest_framework.response import Response

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizRating
        fields = (
            'pk',
            'date',
            'theory',
            'practice',
            'topic',
            'student',
        )

        read_only_fields = ('pk', )


    # def validate_theory(self, value):
    #     if value and value > 100 :
    #         # raise serializers.ValidationError("Theory must not be greater than 100")
    #         value = 100
    #     return value

    def validate(self, data):
        if data:
            if data['topic']:
                # print(data['topic'].pk)
                # print(data['topic'].title)
                # print(data['topic'].subject)
                try:
                    quizConfig = QuizConfig.objects.get(subject=data['topic'].subject)
                except:
                    quizConfig = None
                if quizConfig:
                    if not quizConfig.theory:
                        data['theory'] = 0
                    if not quizConfig.practice:
                        data['practice'] = 0
                if data['student']:
                    groups_student = GroupStudent.objects.filter(student=data['student'])
                    subjects = []
                    for group_student in groups_student:
                        subjects.append(group_student.group.subject)
                    if data['topic'].subject not in subjects:
                        raise serializers.ValidationError('errrrrrr')
        return data


    def to_representation(self, instance):
        data = super(QuizSerializer, self).to_representation(instance)
        if instance.topic:
            data['topic_detail'] = {
                'pk': instance.topic.pk,
                'title': instance.topic.title,
            }
        if instance.student:
            data['student_detail'] = {
                'pk': instance.student.info.pk,
                'first_name': instance.student.info.first_name,
                'last_name': instance.student.info.last_name
            }


        return data


class RealTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealTest
        fields = (
            'pk',
            'date',
            'score',
            'subject',
            'student',

        )

        read_only_fields = ('pk', )



    def to_representation(self, instance):
        data = super(RealTestSerializer, self).to_representation(instance)
        if instance.subject:
            data['subject_detail'] = {
                'pk': instance.subject.pk,
                'title': instance.subject.title,

            }
        if instance.student:
            data['student_detail'] = {
                'pk': instance.student.info.pk,
                'first_name': instance.student.info.first_name,
                'last_name': instance.student.info.last_name,

            }


        return data



class StudentAttSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = ['pk', 'att', 'rating', 'group_student', ]

        read_only_fields = ('pk', )


class GroupAttSerializer(serializers.ModelSerializer):
    student_att = StudentAttSerializer(many=True)

    class Meta:
        model = GroupAttendance
        fields = ['pk', 'date', 'group', 'student_att', ]

        read_only_fields = ('pk', )


    def create(self, validated_data):
        students_data = validated_data.pop('student_att')
        group_data = GroupAttendance.objects.create(**validated_data)
        for student_data in students_data:
            StudentAttendance.objects.create(group_att=group_data, **student_data)
        return group_data