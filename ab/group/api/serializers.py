from rest_framework import serializers
from group.models import Group, GroupStudent

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'pk',
            'title',
            'subject',
            'teacher',
        )
        read_only_fields = ('pk', )


class GroupStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupStudent
        fields = (
            'pk',
            'student',
            'group',
        )

        read_only_fields = ('pk', )