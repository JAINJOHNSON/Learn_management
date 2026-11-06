

from rest_framework import serializers

from django.contrib.auth.models import User

from course_management.models import Course

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id","username","password","email"]
        read_only_fields = ["id"]


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"
        read_only_fields = ["id","created_at"]