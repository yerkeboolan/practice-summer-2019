from rest_framework import serializers
from userInfo.models import Student


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
