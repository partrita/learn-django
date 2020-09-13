from django.db import models
from django.urls import reverse

class Manager(models.Model):
    name = models.CharField(max_length=10)
    contact = models.EmailField()

    def __str__(self):
        return self.name

class Equipment(models.Model):
    model_name = models.CharField(max_length=20)
    model_number = models.CharField(max_length=20)
    manager = models.ForeignKey("Manager", on_delete=models.CASCADE)
    # event = models.ForeignKey('Event', on_delete=SET.NULL)

    def __str__(self):
        return self.model_name

    # def get_absolute_url(self):
    #     return reverse("equip_detail", kwargs={"pk": self.pk})

class Event(models.Model):
    title = models.CharField(max_length=20)
    start_date = models.DateTimeField('Staring time', help_text='Start time')
    end_date = models.DateTimeField('End time', help_text='End time')
    notes = models.TextField('Textual notes', help_text='Text note', blank=True, null=True)
    equip = models.ForeignKey('Equipment', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title
    