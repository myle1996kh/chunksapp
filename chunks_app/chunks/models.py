from django.db import models
from django.contrib.auth.models import User

# ✅ 1️⃣ Model for Blurry Sound Lessons
class BlurryLesson(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()  # The correct sentence
    audio_path = models.FileField(upload_to='blurry_audio/')  # AI-generated blurry audio
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ✅ 2️⃣ Model for ERE (Listen & Repeat) Lessons
class ERELesson(models.Model):
    title = models.CharField(max_length=255)
    phrase = models.TextField()  # The phrase the user must repeat
    audio_path = models.FileField(upload_to='ere_audio/')  # AI-generated phrase
    difficulty = models.CharField(max_length=20, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ✅ 3️⃣ Model for Sound Check Lessons
class SoundCheckLesson(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()  # Sentence for grammar check
    audio_path = models.FileField(upload_to='sound_check_audio/')  # AI-generated sentence
    correct_answer = models.BooleanField()  # True/False question
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ✅ 4️⃣ Model to Store User Recordings (For All Modules)
class UserRecording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson_type = models.CharField(max_length=50, choices=[('blurry', 'Blurry Sound'), ('ere', 'ERE'), ('sound_check', 'Sound Check')])
    lesson_id = models.IntegerField()  # Links to BlurryLesson, ERELesson, or SoundCheckLesson
    audio_path = models.FileField(upload_to='user_recordings/')
    similarity_score = models.FloatField(null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.lesson_type} - {self.similarity_score}%"

# ✅ 5️⃣ Extend Django User Model (For authentication & progress tracking)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    voice_id = models.CharField(max_length=255, blank=True, null=True)  # For voice cloning API
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
