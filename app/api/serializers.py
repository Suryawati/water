from rest_framework import serializers


from water.models import (Premise,
                          MeterInduk,
                          Pump,
                          Valve,
                          AirValve,
                          PMP,
                          FireHydrant,
                          Sipon,
                          TitikBocor,
                          Washout,
                          Pipa)

from land.models import Persil

class PremiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premise
        fields = ['name', 'idpel', 'kode_gol', 'saran']

class MeterIndukSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterInduk
        fields = ['id_meter_induk']

class PumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pump
        fields = ['id_pompa']

class ValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valve
        fields = ['id_valve', 'status_koneksi']

class AirValveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirValve
        fields = ['id_valve', 'status_koneksi']

class PMPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PMP
        fields = ['id', 'name']

class FireHydrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireHydrant
        fields = ['id', 'name']

class SiponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sipon
        fields = ['id', 'sipon_name']

class WashoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Washout
        fields = ['id', 'tipe']

class PipaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipa
        fields = ['id_pipa', 'pemilik', 'kelas_pipa', 'status', 'diameter_pipa', 'material_pipa']

class PersilSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persil
        fields = ['nomor_pelanggan', 'nomor_persil', 'keterangan', 'modify_by']
        #read_only_fields = ['modify_by']

