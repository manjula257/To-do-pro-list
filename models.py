from django.db import models

class todolist(models.Model):
    priority_choices=(('high','high'),('medium','medium'),('low','low'),)
    task_name=models.CharField(max_length=255)
    priority=models.CharField(choices=priority_choices, max_length=100)
    is_done = models.BooleanField(default=False)

def __str__(self):
    return self.task_name


class Reg(models.Model):
    uname=models.EmailField(max_length=20)
    upass=models.CharField(max_length=20)
    ucpass=models.CharField(max_length=20)

class Log(models.Model):
    uname=models.EmailField(max_length=20)
    upass=models.CharField(max_length=20)