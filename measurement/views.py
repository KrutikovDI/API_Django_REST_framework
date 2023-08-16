# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer

# создаем датчик
class New_sensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

# обновляем датчик
class Patch_sensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def patch(self, request):
        request.serializer_class.save()
        return Response({'status': 'ok'})

#  добавление измерения
class Post_measurementView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        request.serializer_class.save()
        return Response({'status': 'OK'})

# получение датчиков
class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

# получение информации по датчику
class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer
