from rest_framework import serializers
from .models import Staff


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

    def validate(self, data):
        if data['role'] != 'manager' and not data.get('approved_by_manager', False):
            raise serializers.ValidationError(
                "Non-manager roles must be approved by a manager.")
        return data
