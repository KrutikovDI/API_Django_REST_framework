# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class New_sensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def post(self, request, name, description):
        Sensor(name=name, description=description).save()
        return Response({'status': 'OK'})

class Patch_sensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def patch(self, sensor, description):
        Sensor(pk=sensor, description=description).save()
        return Response({'status': 'OK'})

class Post_measurement(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, sensor, temperature):
        Measurement(pk=sensor, temperature=temperature).save()
        return Response({'status': 'OK'})


class Measurement(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
