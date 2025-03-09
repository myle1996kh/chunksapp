from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import BlurryLesson, SoundCheckLesson, ERELesson
from .serializers import BlurryLessonSerializer, SoundCheckLessonSerializer, ERELessonSerializer
from .utils.audio_processing import process_audio_and_compare

# ✅ API: Lấy danh sách tất cả bài học Blurry Sound
@api_view(['GET'])
def get_blurry_lessons(request):
    lessons = BlurryLesson.objects.all()
    serializer = BlurryLessonSerializer(lessons, many=True)
    return Response(serializer.data)

# ✅ API: Lấy danh sách tất cả bài học Sound Check
@api_view(['GET'])
def get_soundcheck_lessons(request):
    lessons = SoundCheckLesson.objects.all()
    serializer = SoundCheckLessonSerializer(lessons, many=True)
    return Response(serializer.data)

# ✅ API: Lấy danh sách tất cả bài học ERE
@api_view(['GET'])
def get_ere_lessons(request):
    lessons = ERELesson.objects.all()
    serializer = ERELessonSerializer(lessons, many=True)
    return Response(serializer.data)

# ✅ API: Lấy một bài học Blurry Sound theo ID
@api_view(['GET'])
def get_blurry_lesson(request, lesson_id):
    lesson = get_object_or_404(BlurryLesson, id=lesson_id)
    serializer = BlurryLessonSerializer(lesson)
    return Response(serializer.data)

# ✅ API: So sánh âm thanh user với bài học Blurry Sound
@api_view(['POST'])
def compare_audio(request):
    data = request.data
    lesson_id = data.get("lesson_id")
    user_audio_path = data.get("user_audio_path")

    if not lesson_id or not user_audio_path:
        return Response({"status": "error", "message": "Thiếu lesson_id hoặc file âm thanh"}, status=400)

    lesson = get_object_or_404(BlurryLesson, id=lesson_id)
    similarity_score = process_audio_and_compare(lesson.audio_drive_id, user_audio_path)

    return Response({"similarity_score": similarity_score})
