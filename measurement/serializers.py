from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


# class SensorDetailSerializer(serializers.ModelSerializer):
#     measurements = MeasurementSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description', 'measurements']
#
# class SensorSerializer(serializers.Serializer):
#     # measurements = MeasurementSerializer(read_only=True, many=True)
#     name = serializers.CharField(max_length=50, )
#     description = serializers.CharField(max_length=50, )


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', ]