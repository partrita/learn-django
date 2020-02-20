from django.db import models
from django.forms import ModelForm
from math import pi

class Vib1Input(models.Model):
    A = models.FloatField(
        verbose_name=' amplitude (m)', default=1.0)
    b = models.FloatField(
        verbose_name=' damping coefficient (kg/s)', default=0.0)
    w = models.FloatField(
        verbose_name=' frequency (1/s)', default=2*pi)
    T = models.FloatField(
        verbose_name=' time interval (s)', default=18)

class Vib1InputForm(ModelForm):
    class Meta:
        model = Vib1Input
        fields = ('A','b','w','T')

class SimpleInput(models.Model):
    x = models.FloatField(
        verbose_name='value of x')
    y = models.FloatField(
        verbose_name='value of y')
    z = models.FloatField(
        verbose_name='value of z')

class Tool1Form(ModelForm):
    class Meta:
        model = SimpleInput
        fields = ('x','y')

class Tool2Form(ModelForm):
    class Meta:
        model = SimpleInput
        fields = ('x','y','z')

class Tool3Form(ModelForm):
    class Meta:
        model = SimpleInput
        fields = ('x','y','z')