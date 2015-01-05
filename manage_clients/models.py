import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Psychologist(models.Model):
    def __str__(self):
        return self.name

    EXPERIENCE_CHOICES = (
        ('N', 'novice'),
        ('I', 'intermmediate'),
        ('E', 'experienced'),
    )
    name = models.CharField(max_length=100)
    session_price = models.IntegerField()
    experience_level = models.CharField(max_length=1,
                                        choices=EXPERIENCE_CHOICES)


class Patient(models.Model):
    def __str__(self):
        return self.name

    ILLNESS_CHOICES = (
        ('AF_D', 'affective disorders'),
        ('ANX_D', 'anxiety disorders'),
        ('DD', 'developmental disorders'),
        ('PD', 'personality disorders'),
        ('MH', 'adjustment and minor problems'),
    )
    psychologist = models.ForeignKey(Psychologist)
    name = models.CharField(max_length=100)
    illness = models.CharField(max_length=10, choices=ILLNESS_CHOICES)
    age = models.IntegerField()
    next_session = models.DateTimeField('session reservation')
    experience = models.TextField(default='', blank=True)


class PsychOpinion(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200, unique=True)
    body_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
