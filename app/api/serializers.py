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

from land.models import Persil

class PremiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premise
        fields = ['name', 'idpel', 'kode_gol', 'saran']


class AirValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirValve
        fields = ['id_valve', 'status_koneksi']


class ValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valve
        fields = ['id_valve', 'status_koneksi']

class PersilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persil
        fields = ['nomor_pelanggan', 'nomor_persil', 'keterangan']

class PumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pump
        fields = ['id_pompa']

class PipaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipa
        fields = ['id_pipa', 'pemilik', 'kelas_pipa', 'status', 'diameter_pipa', 'material_pipa']


