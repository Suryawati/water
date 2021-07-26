from django.contrib.gis.db import models
from django.contrib.auth.models import User

# Create your models here.
class Persil(models.Model):
    nomor_persil = models.CharField(max_length=255, null=True)
    nomor_pelanggan = models.CharField(max_length=255, null=True)
    modify_by = models.CharField(max_length=255, null=True)
    #modify_by = models.ForeignKey(User, default=None)
    modify_date = models.DateTimeField('date published',auto_now=True)
    keterangan = models.CharField(max_length=255, null=True)
    sys_id = models.IntegerField()
    flag = models.IntegerField(null=True, default='0')
    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.PolygonField(null=True)

    # Returns the string representation of the model.
    def __str__(self):

        return self.nomor_pelanggan


class Kelurahan(models.Model):
    nama = models.CharField(max_length=255, null=True)
    kode = models.CharField(max_length=255, null=True)
    modify_by = models.CharField(max_length=255, null=True)
    modify_date = models.DateTimeField(null=True)
    keterangan = models.CharField(max_length=255, null=True)
    sys_id = models.IntegerField(null=True)
    flag = models.IntegerField(null=True, default='0')

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    geom = models.PolygonField(null=True)

    # Returns the string representation of the model.
    def __str__(self):
        return self.nama
