from rest_framework import serializers
from .models import Order, Car, Service, Employee


# class OrderSerializer(serializers.Serializer):
#       id = serializers.IntegerField()
#       clients_name = serializers.CharField(max_length=20)
#       clients_surname = serializers.CharField(max_length=20)
#       car_id = serializers.IntegerField()
#       employee_id = serializers.IntegerField()
#       service_id = serializers.IntegerField()
#
#       def create(self, validated_data):
#         return Order.objects.create(**validated_data)
#
#       def update(self, instance, validated_data):
#             instance.clients_name = validated_data.get('clients_name', instance.clients_name)
#             instance.clients_surname = validated_data.get('clients_surname', instance.clients_surname)
#             instance.car_id = validated_data.get('car_id', instance.car_id)
#             instance.employee_id = validated_data.get('employee_id', instance.employee_id)
#             instance.service_id = validated_data.get('service_id', instance.employee_id)
#             instance.save()
#             return instance

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
      car = serializers.CharField()
      service = serializers.CharField()
      employee = serializers.CharField()

      class Meta:
            model = Order
            fields = "__all__"


class OrderCrateSerializer(serializers.ModelSerializer):
      class Meta:
            model = Order
            fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
      brand = serializers.CharField()
      class Meta:
            model = Car
            fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
      class Meta:
            model = Employee
            fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):

      class Meta:
            model = Service
            fields = "__all__"





