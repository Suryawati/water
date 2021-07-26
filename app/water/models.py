from django.contrib.gis.db import models

# Create your models here.
class AirValve(models.Model):
    id_valve = models.CharField(
        help_text=('data id_valve berupa string yang menunjukan identitas '
                  'Contoh AV 101'),
        max_length=255,
        null=True, )

    status_koneksi = models.CharField(
        help_text=('isi OPEN atau'
                   'CLOSE'),
        max_length=255,
        null=True)

    elevasi = models.FloatField(
        help_text='elevasi dalam satuan meter.',
        null=True)

    sys_id = models.IntegerField(
        help_text='digunakan untuk koneksi dengan aplikasi desktop',
        null=True)

    jumlah_putaran = models.FloatField(
        help_text='merupakan maksimal putaran valve dalam 1 x 360 degree',
        null=True)

    merek = models.CharField(
        help_text='Brand valve yang digunakan dan terdaftar dalam daftar katalog',
        max_length=255, null=True)
    chamber_type = models.CharField(max_length=255, null=True)
    arah_putaran = models.CharField(max_length=255, null=True)
    ukuran_valve = models.FloatField(null=True)
    jenis_valve = models.CharField(max_length=255, null=True)

    # Tanggal
    tanggal_pasang = models.DateTimeField(null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)

    modify_by = models.CharField(max_length=255, null=True)
    keterangan = models.CharField(max_length=255, null=True)
    chamber_structure = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    chamber_shape = models.CharField(max_length=255, null=True)
    flag = models.IntegerField(null=True)

    # GeoDjango-specific: a geometry field
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.id_valve


class Valve(models.Model):
    id_valve = models.CharField(max_length=255, null=True)
    status_koneksi = models.CharField(max_length=255, null=True)
    elevasi = models.FloatField(null=True)
    sys_id = models.IntegerField(null=True)
    jumlah_putaran = models.FloatField(null=True)
    merek = models.CharField(max_length=255, null=True)
    chamber_type = models.CharField(max_length=255, null=True)
    arah_putaran = models.CharField(max_length=255, null=True)
    ukuran_valve = models.FloatField(null=True)
    jenis_valve = models.CharField(max_length=255, null=True)
    tanggal_pasang = models.DateTimeField(null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)
    modify_by = models.CharField(max_length=255, null=True)
    keterangan = models.CharField(max_length=255, null=True)
    chamber_structure = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    chamber_shape = models.CharField(max_length=255, null=True)
    flag = models.IntegerField(null=True)

    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.id_valve


class MeterInduk(models.Model):
    distribusi = models.CharField(max_length=255, null=True)
    kelas_meter = models.CharField(max_length=255, null=True)
    sys_id = models.IntegerField(null=True)
    merek_meter = models.CharField(max_length=255, null=True)
    diameter = models.FloatField(null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)
    elevasi = models.FloatField(null=True)
    ketr_lokasi = models.CharField(max_length=255, null=True)
    jenis_meter = models.CharField(max_length=255, null=True)
    modify_by = models.CharField(max_length=255, null=True)
    tanggal_bongkar = models.DateTimeField(null=True)
    id_meter_induk = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    tanggal_pasang = models.DateTimeField(null=True)
    keterangan = models.CharField(max_length=255, null=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PointField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.id_meter_induk

class Pump(models.Model):
    id_pompa  = models.CharField(max_length=255, null=True)
    elevasi = models.FloatField(null=True)
    merek = models.CharField(max_length=255, null=True)
    head = models.IntegerField(null=True)
    function = models.CharField(max_length=255, null=True)
    diameter = models.IntegerField(null=True)
    modify_by = models.CharField(max_length=255, null=True)
    voltase = models.IntegerField(null=True)
    sys_id = models.IntegerField(null=True)
    kecepatan = models.IntegerField(null=True)
    kapasitas = models.FloatField(null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)
    tipe = models.CharField(max_length=255, null=True)
    serial = models.CharField(max_length=255, null=True)
    daya = models.IntegerField(null=True)
    total_head = models.IntegerField(null=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PoinField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return str(self.id)

class PMP(models.Model):
    modify_by  = models.CharField(max_length=255, null=True)
    remarks = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    sys_id = models.IntegerField(null=True)
    alamat = models.CharField(max_length=255, null=True)
    install_date = models.DateTimeField(null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

class FireHydrant(models.Model):
    modify_date = models.DateTimeField(null=True)
    modify_by = models.CharField(max_length=255, null=True)
    install_date = models.DateTimeField('date published',auto_now=True)
    sys_id = models.IntegerField(null=True)
    hydrant_size = models.FloatField(null=True)
    status = models.CharField(max_length=255, null=True)
    hydrant_type = models.CharField(max_length=255, null=True)
    keterangan = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Pipa(models.Model):
    elevasi_1 = models.FloatField(null=True)
    function = models.CharField(max_length=255, null=True)
    elevasi = models.FloatField(null=True)
    sys_id = models.IntegerField(null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)
    pelapisan_pipa = models.CharField(max_length=255, null=True)
    diameter_pipa = models.FloatField(null=True)
    id_pipa = models.CharField(max_length=255, null=True)
    id_symbol = models.IntegerField(null=True)
    elevasi_2 = models.FloatField(null=True)
    material_pipa = models.CharField(max_length=255, null=True)
    pemilik = models.CharField(max_length=255, null=True)
    kelas_pipa = models.CharField(max_length=255, null=True)
    modify_by = models.CharField(max_length=255, null=True)
    roughness = models.FloatField(null=True)
    pjg_pipa_kalkulasi = models.FloatField(null=True)
    pjg_pipa_geometris = models.FloatField(null=True)
    status = models.CharField(max_length=255, null=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.LineStringField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return str(self.id)

class Sipon(models.Model):
    modify_date = models.DateTimeField('date published',auto_now=True)
    modify_by = models.CharField(max_length=255, null=True)
    sipon_name = models.CharField(max_length=255, null=True)
    length = models.FloatField(null=True)
    install_date = models.DateTimeField(null=True)
    buffer_type = models.CharField(max_length=255, null=True)
    sys_id = models.IntegerField(null=True)
    id_sipon = models.CharField(max_length=50, null=True)
    surface_area = models.FloatField(null=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.sipon_name


class Washout(models.Model):
    jumlah_putaran = models.FloatField(null=True)
    tanggal_terpasang = models.DateTimeField(null=True)
    letak = models.CharField(max_length=255, null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)
    elevasi = models.FloatField(null=True)
    sys_id = models.IntegerField(null=True)
    id_washout = models.CharField(max_length=255, null=True)
    chamber_structure = models.CharField(max_length=255, null=True)
    tipe = models.CharField(max_length=255, null=True)
    chamber_type = models.CharField(max_length=255, null=True)
    chamber_shape = models.CharField(max_length=255, null=True)
    modify_by = models.CharField(max_length=255, null=True)
    ukuran = models.FloatField(null=True)
    keterangan = models.CharField(max_length=255, null=True)
    washout_supplier = models.CharField(max_length=255, null=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.id_washout


class TitikBocor(models.Model):
    modify_date = models.DateTimeField('date published',auto_now=True)
    tanggal_bocor = models.DateTimeField(null=True)
    modify_by = models.CharField(max_length=255, null=True)
    nama_obyek = models.CharField(max_length=255, null=True)
    jenis_pipa = models.CharField(max_length=255, null=True)
    sys_id = models.IntegerField(null=True)
    diameter_pipa = models.FloatField(null=True)
    jenis_obyek = models.CharField(max_length=255, null=True)
    tanggal_perbaikan = models.DateTimeField(null=True)
    flag = models.IntegerField(null=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.nama_obyek


class Premise(models.Model):
    """Premise berisi data Pelanggan."""
    premise_type = models.CharField(max_length=255, null=True)
    consumption = models.CharField(max_length=255, null=True)
    idpel = models.CharField(max_length=255, null=True)
    sys_id = models.IntegerField(null=True)
    cater_date = models.CharField(max_length=255, null=True)
    longitude = models.FloatField(null=True)
    address2 = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    meter_location = models.CharField(max_length=255, null=True)
    kode_gol = models.CharField(max_length=255, null=True)
    latitude = models.FloatField(null=True)
    address1 = models.CharField(max_length=255, null=True)
    modify_by = models.CharField(max_length=255, null=True)
    kelurahan = models.CharField(max_length=255, null=True)
    elevation = models.FloatField(null=True)
    name = models.CharField(max_length=255, null=True)
    kabupaten = models.CharField(max_length=255, null=True)
    kecamatan = models.CharField(max_length=255, null=True)
    mr_officer = models.CharField(max_length=255, null=True)
    kode_lokasi = models.CharField(max_length=255, null=True)
    address3 = models.CharField(max_length=255, null=True)
    noreg = models.CharField(max_length=255, null=True)
    modify_date = models.DateTimeField('date published',auto_now=True)
    water_meter = models.CharField(max_length=255, null=True)
    remarks = models.CharField(max_length=255, null=True)
    """field baru dari mysql"""
    jlw = models.CharField(max_length=255, null=True)
    urljlw = models.CharField(max_length=255, null=True)
    urljlwp = models.CharField(max_length=255, null=True)
    stat_sam = models.CharField(max_length=255, null=True)
    usrt_sam = models.CharField(max_length=255, null=True)
    dia_met = models.CharField(max_length=255, null=True)
    no_met = models.CharField(max_length=255, null=True)
    merk_met = models.CharField(max_length=255, null=True)
    flag = models.IntegerField(default=0)
    saran = models.CharField(max_length=255, null=True)
    # GeoDjango-specific: a geometry field (PolygonField)
    geom = models.PointField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.flag is None:
            self.flag = 0
        else :
            self.flag = self.flag + 1

        super().save(*args, **kwargs)  # Call the "real" save() method.
