# django lib
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.generic import TemplateView

from django.db.models import Count
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
# 3rd party lib
from djgeojson.views import GeoJSONLayerView
import json

# local
from land.models import Kelurahan
from water.models import AirValve, FireHydrant, MeterInduk, Pipa, PMP, Premise, Pump, Sipon, TitikBocor, Valve, Washout

def pelanggan_dummy(request):

    # do something with the your data
    data = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        116.82673177895003,
                        -1.234395306610765
                    ]
                },
                "properties": {
                    "XTRID": "337533",
                    "LATITUDE": -1.2343952656,
                    "LONGITUDE": 116.8267288208,
                    "NAMA": "AGUS PRATONO",
                    "ORI": 0.0,
                    "SYMBOLOGIE": "6"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        116.82504748552788,
                        -1.2326549611023954
                    ]
                },
                "properties": {
                    "XTRID": "342831",
                    "LATITUDE": -1.2326550484,
                    "LONGITUDE": 116.825050354,
                    "NAMA": "SUPARDI",
                    "ORI": 0.0,
                    "SYMBOLOGIE": "6"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        116.82413402085479,
                        -1.233047007446097
                    ]
                },
                "properties": {
                    "XTRID": "342991",
                    "LATITUDE": -1.2330470085,
                    "LONGITUDE": 116.8241348267,
                    "NAMA": "EDDY AYUB",
                    "ORI": 0.0,
                    "SYMBOLOGIE": "6"
                }
            },
        ]
    }


    # just return a JsonResponse
    return JsonResponse(data)

class LatLonRadMixin:
    def get_lat_lon_rad(self, **kwargs):
        lati = self.kwargs.get('lati')
        long = self.kwargs.get('long')
        meter_rad = self.kwargs.get('meter')
        if not (lati and long and meter_rad):
            return HttpResponseBadRequest(
                'Request must include latitude, longitude and radius value')
        try:
            point = Point(float(long), float(lati))
            meter_rad = int(meter_rad)
        except ValueError as err:
            raise Exception(
                'latitude and longitude must in float, '
                'radius must in integer meter.'
            ) from err
        return (point, meter_rad)


class AirValveLayer(GeoJSONLayerView, LatLonRadMixin):
    def get_queryset(self, **kwargs):
        point, meter_rad = self.get_lat_lon_rad(**kwargs)
        context = AirValve.objects.filter(
            geom__distance_lt=(point, Distance(m=meter_rad)))
        return context


class FireHidrantLayer(GeoJSONLayerView, LatLonRadMixin):
    def get_queryset(self, **kwargs):
        point, meter_rad = self.get_lat_lon_rad(**kwargs)
        context = FireHidrantLayer.objects.filter(
            geom__distance_lt=(point, Distance(m=meter_rad)))
        return context


class MeterIndukLayer(GeoJSONLayerView, LatLonRadMixin):
    def get_queryset(self, **kwargs):
        point, meter_rad = self.get_lat_lon_rad(**kwargs)
        context = MeterInduk.objects.filter(
            geom__distance_lt=(point, Distance(m=meter_rad)))
        return context


class PMPLayer(GeoJSONLayerView, LatLonRadMixin):
    def get_queryset(self, **kwargs):
        point, meter_rad = self.get_lat_lon_rad(**kwargs)
        context = PMP.objects.filter(
            geom__distance_lt=(point, Distance(m=meter_rad)))
        return context


class KelurahanLayer(GeoJSONLayerView):
    def get_queryset(self):
        context = Kelurahan.objects.all()
        return context


class PremiseLayer(GeoJSONLayerView, LatLonRadMixin):
    def get_queryset(self, **kwargs):
        point, meter_rad = self.get_lat_lon_rad(**kwargs)
        context = Premise.objects.filter(
            geom__distance_lt=(point, Distance(m=meter_rad)))
        return context

class PumpLayer(GeoJSONLayerView, LatLonRadMixin):
    def get_queryset(self, **kwargs):
        point, meter_rad = self.get_lat_lon_rad(**kwargs)
        context = Pump.objects.filter(
            geom__distance_lt=(point, Distance(m=meter_rad)))
        return context

class PipaLayer(GeoJSONLayerView, LatLonRadMixin):
    def get_queryset(self, **kwargs):
        point, meter_rad = self.get_lat_lon_rad(**kwargs)
        context = Pipa.objects.filter(
            geom__distance_lte=(point, Distance(m=meter_rad)))
        return context

def ambil_data(request):

    query = MeterInduk.objects.values('status').annotate(total=(Count('*')))
    #data = Premise.objects.all()
    data = json.dumps(list(query))
    #users_list = list(query)
    return JsonResponse({'data': data})
    #return render(request, 'dashboard.html', contex={'data':data})
