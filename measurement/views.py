# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Sensor
from .serializers import SensorSerializer

@api_view(['GET'])
def meas(request):
    sensors = Sensor.objects.all()
    ser = SensorSerializer(sensors, many=True)
    # data = {'message': 'Hello'}
    return Response(ser.data)

print('aaa')