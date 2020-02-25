from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120, help_text='메세지의 제목')
    message = models.TextField(help_text='니 생각은 어때?')

    def __str__(self):
        return self.title
