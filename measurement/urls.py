from django.urls import path


from .views import New_sensorView, Patch_sensor, Post_measurement, Measurement

urlpatterns = [
    path('new_sensor/<name>/<description>/', New_sensorView.as_view()),
    path('patch_sensor/<sensor>/<description>/', Patch_sensor.as_view()),
    path('post_measurement/<sensor>/<temperature>/', Post_measurement.as_view()),
    path('measurement/<pk>/', Measurement.as_view()),

]

