from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    description = models.CharField(blank=True, verbose_name='описание')


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата/время создания')
