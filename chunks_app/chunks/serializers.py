from rest_framework import serializers
from .models import BlurryLesson, SoundCheckLesson, ERELesson

class BlurryLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlurryLesson
        fields = '__all__'  # Hoặc chọn ['id', 'title', 'audio_drive_id', ...]

class SoundCheckLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundCheckLesson
        fields = '__all__'

class ERELessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ERELesson
        fields = '__all__'
