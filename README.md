# Django-Geoloc with docker-compose

## Prerequisites
- Git
- Docker

## Tech
- docker compose
- python3
    - django
    - django-bootstrap
    - django-geojson
    - django-leaflet
    - gunicorn
- nginx
- postGIS

---
### Development environment

Build and spin up docker-compose

```
$ docker-compose up -d --build
```

### Production environment

1. Build and spin up docker-compose using additional Compose file with -f option
2. Migrate database
3. Collect staticfiles

```
$ docker-compose -f docker-compose.prod.yml up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
$ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

4. Create superuser to access admin page
```
$ docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

```
$ docker-compose -f docker-compose.prod.yml logs
```

explore running web container
```
$ docker-compose -f docker-compose.prod.yml exec web sh 
```

----

## Insert records dari JSON ke Postgres
```
ogr2ogr -f "PostgreSQL" PG:"host='localhost' dbname=django_geoloc_dev user=django_geoloc port=35432 password=django_geoloc" data/air-valve.geojson -nln water_airvalve -append
```

```
ogr2ogr -f "PostgreSQL" PG:"host='localhost' dbname=django_geoloc_dev user=django_geoloc port=35432 password=django_geoloc" Water_Fire_Hydrant_Lokasi.shp -nln water_firehydrant -append -sql "SELECT DIUPDATE_O as modify_date, DIUPDATE_T as modify_date, KETERANGAN as keterangan, NAMA_HYDRA as name, STATUS as status, TANGGAL_PA as install_date, TIPE_HYDRA as hydrant_type, UKURAN_HYD as hydrant_size, SYS_ID as rwo_id, ORI as location_geometry, SYMBOLOGIE as flag FROM Water_Fire_Hydrant_Lokasi"
ogr2ogr -f "PostgreSQL" PG:"host='localhost' dbname=django_geoloc_dev user=django_geoloc port=35432 password=django_geoloc" Water_Meter_Induk_Lokasi.shp -nln water_meterinduk -append -sql "SELECT DIAMETER as diameter, DISTRIBUSI as distribusi, DIUPDATE_O as modify_date, DIUPDATE_T as modify_date, KETERANGAN as keterangan, ELEVASI as elevasi, ID_METER_I as id_meter_induk, JENIS_METE as jenis_meter, KELAS_METE as kelas_meter, STATUS as status, MEREK_METE as merek_meter, TANGGAL_BO as tanggal_bongkar, TANGGAL_PA as tanggal_pasang, SYS_ID as rwo_id, ORI as location_geometry, SYMBOLOGIE as flag FROM Water_Meter_Induk_Lokasi"
ogr2ogr -f "PostgreSQL" PG:"host='localhost' dbname=django_geoloc_dev user=django_geoloc port=35432 password=django_geoloc" Water_Pipa_Geometri.shp -nln water_pipa -lco GEOMETRY_NAME=path_geometry -append -sql "SELECT DIAMETER_P as diameter_pipa,  DIUPDATE_O as modify_date, DIUPDATE_T as modify_date, ELEVASI as elevasi, ELEVASI_1 as elevasi_1, ELEVASI_2 as elevasi_2, FUNGSI as function, ID_PIPA as id_pipa, KELAS_PIPA as kelas_pipa, MATERIAL_P as material_pipa, PANJANG_PI as pjg_pipa_geometris, PANJANG_P1 as pjg_pipa_kalkulasi, PELAPISAN_ as pelapisan_pipa, PEMILIK as pemilik, ROUGHNESS as roughness , SYS_ID as rwo_id, STATUS as status, SYMBOLOGIE as flag FROM Water_Pipa_Geometri" 
ogr2ogr -f "PostgreSQL" PG:"host='localhost' dbname=django_geoloc_dev user=django_geoloc port=35432 password=django_geoloc" Land_Kelurahan_Boundary.shp -nln land_kelurahan -lco GEOMETRY_NAME=path_geometry -sql "SELECT DIUPDATE_O as modify_date, DIUPDATE_T as modify_date,  KETERANGAN as keterangan, KODE as kode, NAMA_KELUR as nama, SYS_ID as rwo_id, SYMBOLOGIE as flag FROM Land_Kelurahan_Boundary" 

```