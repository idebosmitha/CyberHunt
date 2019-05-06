from django.db import models


class Team(models.Model):
    teamname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name1 = models.CharField(max_length=50)
    year1 = models.IntegerField()
    dept1 = models.CharField(max_length=10)
    phone1 = models.BigIntegerField()
    name2 = models.CharField(max_length=50)
    year2 = models.IntegerField()
    dept2 = models.CharField(max_length=10)
    phone2 = models.BigIntegerField()


    def __str__(self):
        return self.teamname
