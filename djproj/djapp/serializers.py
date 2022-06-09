from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'student_track']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['track_title'] = instance.student_track.title
        return rep


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['track_title']
