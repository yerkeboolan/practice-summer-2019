from configuration.models import UserStatusConfig, QuizConfig
from rest_framework import serializers

class UserStatusConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatusConfig
        fields = (
            'pk',
            'status',
            'is_active',
            'description'
        )

        read_only_fields = ('pk', )

class QuizConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizConfig
        fields = (
            'pk',
            'subject',
            'practice',
            'theory',
        )


        read_only_fields = ('pk', )
