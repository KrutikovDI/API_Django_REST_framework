from django.urls import path


from .views import New_sensorView, Patch_sensorView, Post_measurementView, Measurement, SensorsView, SensorView

urlpatterns = [
    path('new_sensor/', New_sensorView.as_view()),
    path('patch_sensor/<pk>/', Patch_sensorView.as_view()),
    path('post_measurement/', Post_measurementView.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),

]

