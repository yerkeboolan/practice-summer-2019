from rest_framework import serializers
from userInfo.models import Student
from studentProgress.models import QuizRating

class StudentSerializerInfo(serializers.ModelSerializer):
    class Meta:
        model = Student

    def to_representation(self, instance):
        data = {
            'pk': instance.info.pk,
            'first_name': instance.info.first_name,
            'last_name': instance.info.last_name,
            'email': instance.info.email,
            'is_active': instance.info.is_active
        }
        if instance.status:
            data['status'] = instance.status.status
            data['status_description'] = instance.status.description
        else:
            data['status'] = None

        groups = instance.student_group.all()
        if groups:
            data['groups'] = []
            for group_student in groups:
                cur = {
                    'pk': group_student.pk,
                    'title': group_student.group.title,
                    'subject': group_student.group.subject.title,
                    'teacher': group_student.group.teacher.info.first_name + " " +
                               group_student.group.teacher.info.last_name,
                }
                # print(cur)
                data['groups'].append(cur)
        return data

class StudentStatusSerializer(serializers.Serializer):
    status = serializers.IntegerField()


class StudentGroupSerializerInfo(serializers.ModelSerializer):
    class Meta:
        model = Student

    def to_representation(self, instance):
        data = {
            'student': {
                'pk': instance.pk,
                'name': instance.info.first_name,
                'surname': instance.info.last_name
            }
        }

        groups = instance.student_group.all()
        if groups:
            data['group'] = []
            for group_student in groups:
                cur = {
                    'pk': group_student.group.pk,
                    'title': group_student.group.title,
                    'subject': {
                        'pk': group_student.group.subject.pk,
                        'title': group_student.group.subject.title
                    },
                    'teacher': {
                        'pk': group_student.group.teacher.info.pk,
                        'name': group_student.group.teacher.info.first_name,
                        'surname': group_student.group.teacher.info.last_name
                    },
                    'quiz': []
                }
                topics = group_student.group.subject.topic.all()
                # select * from quiz_rating where topic_id =  and student_id = 2
                student = instance.pk
                for topic in topics:
                    try:
                        quizzes = QuizRating.objects.filter(topic=topic, student=student)
                        current_quiz = {
                            'topic': {
                                'pk': topic.pk,
                                'title': topic.title
                            },
                            'quizzes': []
                        }
                        for quiz in quizzes:
                            quiz = {
                                'pk': quiz.pk,
                                'date': quiz.date,
                                'theory': quiz.theory,
                                'practice': quiz.practice,
                            }
                            current_quiz['quizzes'].append(quiz)
                        cur['quiz'].append(current_quiz)
                    except QuizRating.DoesNotExist:
                        pass
                data['group'].append(cur)
        return data
