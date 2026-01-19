from django.db import models
from rest_framework import permissions


class USER(models.Model):

    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=120, unique=True)

    class Meta:
        db_table = 'USER'
        ordering = ['user_id']

    def __str__(self):
        return self.user_name

class TASK(models.Model):

    task_id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=120)
    assigned_by = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='task_by', to_field='user_name')
    assigned_to = models.ForeignKey(USER, on_delete=models.CASCADE, related_name='task_to', to_field='user_name')
    status = models.CharField(max_length=50, choices=(('running', 'running'), ('completed', 'completed'), ('pending', 'pending')))
    priority = models.CharField(max_length=50, choices=(('low', 'low'), ('medium', 'medium'), ('high', 'high')))

    class Meta:
        db_table = 'TASK'
        ordering = ['priority']
        unique_together = ('task_name', 'assigned_by', 'assigned_to')

    def __str__(self):
        return self.task_name

