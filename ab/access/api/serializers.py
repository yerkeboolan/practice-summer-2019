from rest_framework import serializers
from access.models import VideoAccess, TestAccess


class VideoAccessSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoAccess
        fields = ('pk', 'access', 'video', 'group_student', )

        read_only_fields = ('pk', )

class TestAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestAccess
        fields = ('pk', 'access', 'test', 'group_student', )

        read_only_fields = ('pk', )


    def validate(self, data):
        try:
            video_access = VideoAccess.objects.get(group_student=data['group_student'], video__subtopic=data['test'].subtopic)
            if not video_access.access:
                data['access'] = False
        except VideoAccess.DoesNotExist:
            raise serializers.ValidationError('Video does not exist')
        return data