from django.db import models
from .validators import validate_pdf, validate_video


# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class TrackImage(models.Model):
    track = models.ForeignKey(Track, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.image.name


class TrackVideo(models.Model):
    track = models.ForeignKey(Track, related_name='videos', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Video Display Name")
    video = models.FileField(validators=[validate_video])

    def __str__(self):
        return self.name


class Subject(models.Model):
    track = models.ForeignKey(Track, related_name='subjects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    subject = models.ForeignKey(Subject, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pdf = models.FileField(validators=[validate_pdf])
    sequence = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Test(models.Model):
    track = models.ForeignKey(Track, related_name='tests', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    choiceA = models.CharField(max_length=100, blank=True)
    choiceB = models.CharField(max_length=100, blank=True)
    choiceC = models.CharField(max_length=100, blank=True)
    choiceD = models.CharField(max_length=100, blank=True)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question


class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    choiceA = models.CharField(max_length=100, blank=True)
    choiceB = models.CharField(max_length=100, blank=True)
    choiceC = models.CharField(max_length=100, blank=True)
    choiceD = models.CharField(max_length=100, blank=True)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question
