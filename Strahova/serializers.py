from rest_framework import serializers
from .models import DepartmentsMap


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentsMap
        fields = '__all__'
