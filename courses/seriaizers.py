from rest_framework import serializers
from courses.models import Course
from courses.models import Profession

class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'

class ProfessionSeriaizer(serializers.Serializer):
    class Meta:
        model = Profession
        fields = ["title"]