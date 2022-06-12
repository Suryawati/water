from django.urls import path
from django.conf.urls import url

# for leaflet map
from djgeojson.views import GeoJSONLayerView, TiledGeoJSONLayerView

from api.views import assets, updates
from land.models import Kelurahan, Persil
from water.models import Premise, MeterInduk, Pump
from water.models import Valve, AirValve, PMP
from water.models import FireHydrant, Sipon, Washout, Pipa

urlpatterns = [
    path('pelanggan', assets.pelanggan_dummy, name='pelanggan'),

    path('datajson', assets.ambil_data, name='json'),

# map
    path('<lati>/<long>/<int:meter>/premise.geojson', assets.PremiseLayer.as_view(
        model=Premise,
        properties=('id', 'name', 'idpel', 'address1', 'address2', 'kode_lokasi', 'premise_type', 'status', 'kode_gol', 'location_geometry', 'saran')
    ), name='json-premise'),

    path('<lati>/<long>/<int:meter>/meterinduk.geojson', assets.MeterIndukLayer.as_view(
        model=MeterInduk,
        properties=('id', 'id_meter_induk', 'location_geometry')
    ), name='json-meterinduk'),

    path('<lati>/<long>/<int:meter>/pump.geojson', assets.PumpLayer.as_view(
        model=Pump,
        properties=('id', 'id_pompa', 'location_geometry')
    ), name='json-pump'),

    path('<lati>/<long>/<int:meter>/valve.geojson', assets.ValveLayer.as_view(
        model=Valve,
        properties=('id', 'id_valve', 'location_geometry', 'ukuran_valve')
    ), name='json-valve'),

    path('<lati>/<long>/<int:meter>/airvalve.geojson', assets.AirValveLayer.as_view(
        model=AirValve,
        properties=('id', 'id_valve', 'location_geometry', 'ukuran_valve')
    ), name='json-airvalve'),

    path('<lati>/<long>/<int:meter>/pmp.geojson', assets.PMPLayer.as_view(
        model=PMP,
        properties=('id', 'name', 'location_geometry')
    ), name='json-pmp'),

    path('<lati>/<long>/<int:meter>/firehydrant.geojson', assets.FireHydrantLayer.as_view(
        model=Washout,
        properties=('id', 'name', 'location_geometry')
    ), name='json-hydrant'),

    path('<lati>/<long>/<int:meter>/washout.geojson', assets.WashoutLayer.as_view(
        model=Washout,
        properties=('id', 'tipe', 'location_geometry')
    ), name='json-washout'),

    path('<lati>/<long>/<int:meter>/sipon.geojson', assets.SiponLayer.as_view(
        model=Sipon,
        properties=('id', 'sipon_name', 'location_geometry')
    ), name='json-sipon'),

    path('<lati>/<long>/<int:meter>/pipa.geojson', assets.PipaLayer.as_view(
        model=Pipa,
        properties=('id','id_pipa', 'pemilik', 'kelas_pipa', 'location_geometry', 'status', 'diameter_pipa', 'material_pipa', 'pjg_pipa_geometris')
    ), name='json-pipa'),

    path('<lati>/<long>/<int:meter>/persil.geojson', assets.PersilLayer.as_view(
        model=Persil,
        properties=('id', 'nomor_pelanggan', 'location_geometry', 'keterangan')
    ), name='json-persil'),


    path('kelurahan.geojson', assets.KelurahanLayer.as_view(
        model=Kelurahan,
        properties=('nama', 'kode', 'location_geometry')
    ), name='json-kelurahan'),

    # we dont use this one, nice to keep it for future  use
    url(r'^data/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+).geojson$',
    TiledGeoJSONLayerView.as_view(model=Premise, properties=('name', 'address_1')), name='data'),


    #  update data
    path('premise/<int:pk>', updates.PremiseUpdate.as_view(), name='update-premise'),
    path('airvalve/<int:pk>', updates.AirValveUpdate.as_view(), name='update-airvalve'),
    path('valve/<int:pk>', updates.ValveUpdate.as_view(), name='update-valve'),
    path('pipa/<int:pk>', updates.PipaUpdate.as_view(), name='update-pipa'),
    path('pump/<int:pk>', updates.PumpUpdate.as_view(), name='update-pump'),
    path('persil/<int:pk>', updates.PersilUpdate.as_view(), name='update-persil'),
    path('meterinduk/<int:pk>', updates.MeterIndukUpdate.as_view(), name='update-meterinduk'),
]



