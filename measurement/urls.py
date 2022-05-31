from django.urls import path

from measurement.views import meas

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('meas/', meas),  # подключаем маршруты из приложения measurement

]
