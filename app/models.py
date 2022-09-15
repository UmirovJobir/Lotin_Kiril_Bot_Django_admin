from statistics import mode
from unicodedata import category
from django.db import models

class Dictionary(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=30)
    lotin = models.CharField(max_length=200)
    kiril = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Словарь'

    def __str__(self):
        return f"{self.id} {self.category} {self.lotin} {self.kiril}"

    

class Users(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.chat_id} -- {self.username}  --  {self.date}"
