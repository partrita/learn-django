from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

# class Event(models.Model):
#     day = models.DateField('Day of event', help_text='Day of event')
#     start_time = models.TimeField('Staring time', help_text='Start time')
#     end_time = models.TimeField('End time', help_text='End time')
#     notes = models.TextField('Textual notes', help_text='Text note', blank=True, null=True)

#     class Meta:
#         verbose_name = 'Scheduling'
#         verbose_name_plural = 'Scheduling'
    
#     def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
#         overlap = False
#         if new_start == fixed_end or new_end == fixed_start:    #edge case
#             overlap = False
#         elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
#             overlap = True
#         elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
#             overlap = True
 
#         return overlap
 
#     def get_absolute_url(self):
#         url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
#         return u'<a href="%s">%s</a>' % (url, str(self.start_time))
 
#     def clean(self):
#         if self.end_time <= self.start_time:
#             raise ValidationError('Ending times must after starting times')
 
#         events = Event.objects.filter(day=self.day)
#         if events.exists():
#             for event in events:
#                 if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
#                     raise ValidationError(
#                         'There is an overlap with another event: ' + str(event.day) + ', ' + str(
#                             event.start_time) + '-' + str(event.end_time))

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

    # def __str__(self):
    #     return self.model_name

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
    