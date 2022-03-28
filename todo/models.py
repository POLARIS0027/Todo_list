from django.db import models
from datetime import date
import datetime

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=40, verbose_name="할일")
    description = models.TextField(max_length=200, verbose_name="내용")
    date_created = models.DateField(auto_now_add=True, verbose_name="작성일")
    date_deadline = models.DateField(verbose_name="마감일")
    
    def remaining_days(self):
        delta = self.date_deadline - date.today()
        days = delta.days
        if days > 0:
            return f'{days}일 남음'
        elif days == 0:
            return '오늘까지!!'
        else:
            days = abs(days)
            return f'{days}일 지남'
        
    
    def __str__(self):
        return f'{self.name} | {self.description} | {self.date_created} |       {self.date_deadline}'
    
class TodoList_images(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='todo/images/%Y/%m', blank=True)
    
class TodoList_files(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    file = models.FileField(upload_to='todo/files/%Y/%m', blank=True)