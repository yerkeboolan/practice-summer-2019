from configuration.models import UserStatusConfig
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
