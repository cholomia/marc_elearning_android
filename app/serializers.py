from rest_framework import serializers
from .models import Track, Subject, Lesson, Test, Quiz, TrackImage


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TrackImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackImage
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    tests = TestSerializer(many=True, read_only=True)
    images = TrackImageSerializer(many=True, read_only=True)

    class Meta:
        model = Track
        fields = '__all__'
