from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name