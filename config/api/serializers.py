from rest_framework import serializers

from .models import Puples, Class


class PuplesSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(source="course.title", read_only=True)
    class Meta:
        model = Puples
        fields = '__all__'
        # exclude = ['image', 'address']


class ClassSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True)
    class Meta:
        model = Class
        fields = '__all__'