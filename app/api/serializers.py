from rest_framework import serializers

from water.models import (AirValve,
                          FireHydrant,
                          MeterInduk,
                          Pipa,
                          PMP,
                          Premise,
                          Pump,
                          Sipon,
                          TitikBocor,
                          Valve,
                          Washout)



class PremiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premise
        fields = ['name', 'kode_lokasi']


class AirValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirValve
        fields = ['id_valve', 'status_koneksi']


class ValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valve
        fields = ['id_valve', 'status_koneksi']
