from django.contrib import admin
from app.models import Track, Subject, Lesson, Test, Quiz

# Register your models here.
admin.site.register(Track)
admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Test)
admin.site.register(Quiz)