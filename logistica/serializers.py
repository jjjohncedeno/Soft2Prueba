from django.contrib.auth.models import User, Group
from rest_framework import serializers
from logistica.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = ('url', 'username', 'email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields = ('url', 'name')

class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('nDisco', 'tipo', 'marca', 'placa', 'modelo', 'cSentados', 'cParados')

class ConductorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conductor
        fields = ('nombre', 'cedula')

class RutaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ruta
        fields =('nombre', 'tipo')

class HorarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Horario
        fields = ('url', 'ruta', 'bus', 'conductor', 'fechaIncicio', 'fechaFin')
