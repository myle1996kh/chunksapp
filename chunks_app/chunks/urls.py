from django.urls import path
from .views import get_blurry_lessons, get_blurry_lesson, get_soundcheck_lessons, get_ere_lessons, compare_audio

urlpatterns = [
    path('blurry-lessons/', get_blurry_lessons, name="blurry_lessons"),
    path('blurry-lesson/<int:lesson_id>/', get_blurry_lesson, name="blurry_lesson"),
    path('soundcheck-lessons/', get_soundcheck_lessons, name="soundcheck_lessons"),
    path('ere-lessons/', get_ere_lessons, name="ere_lessons"),
    path('compare-audio/', compare_audio, name="compare_audio"),
]
