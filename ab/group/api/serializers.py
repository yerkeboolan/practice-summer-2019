from rest_framework import serializers
from group.models import Group, GroupStudent
from subject.api.serializers import SubjectTopicSerializer

class GroupSerializer(serializers.ModelSerializer):
    # subject = SubjectTopicSerializer(read_only=True)
    class Meta:
        model = Group
        fields = (
            'pk',
            'title',
            'subject',
            'teacher',
        )
        read_only_fields = ('pk', )

    def to_representation(self, instance):
        data = super(GroupSerializer, self).to_representation(instance)
        if instance.subject:
            data['subject_detail'] = {
                'pk': instance.subject.pk,
                'title': instance.subject.title,
                # 'topic': instance.subject.topic,
            }
        if instance.teacher:
            data['teacher_detail'] = {
                'pk': instance.teacher.info.pk,
                'first_name': instance.teacher.info.first_name,
                'last_name': instance.teacher.info.last_name,
            }

        return data

class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = (
            'pk',
            'student',
            'group',
        )

        read_only_fields = ('pk', )

    def to_representation(self, instance):
        data = super(GroupStudentSerializer, self).to_representation(instance)
        if instance.student:
            data['student_detail'] = {
                'pk': instance.student.info.pk,
                'first_name': instance.student.info.first_name,
                'last_name': instance.student.info.last_name,
            }
        if instance.group:
            data['group_detail'] = {
                'pk': instance.group.pk,
                'title': instance.group.title,
            }
        return data