from django.contrib import admin
from .models import BlurryLesson, ERELesson, SoundCheckLesson, UserRecording, UserProfile

# ✅ Register models in the Django admin panel
admin.site.register(BlurryLesson)
admin.site.register(ERELesson)
admin.site.register(SoundCheckLesson)
admin.site.register(UserRecording)
admin.site.register(UserProfile)
