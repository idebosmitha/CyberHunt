from django.db import models

from teams.models import Team


class Question(models.Model):
    name = models.CharField(max_length=50)
    body = models.CharField(max_length=300)
    answer = models.CharField(max_length=100)
    points = models.IntegerField()


    def __str__(self):
        return f'{self.name} [{self.points}]'


class File(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='files/')


class Image(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    image = models.FileField(upload_to='images/')


class Submission(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.team.teamname}: {self.question.name}'
