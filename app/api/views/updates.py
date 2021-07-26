from django.shortcuts import get_object_or_404, redirect
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from django.views.generic import UpdateView
from django.contrib.auth.models import User

from api.serializers import (PremiseSerializer,
                            ValveSerializer,
                             AirValveSerializer,
                             PipaSerializer,
                             PumpSerializer,
                             PersilSerializer,
                             MeterIndukSerializer)

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

class UpdateMixin():
    """
    Model dan serializer yang diupdate.

    Untuk mengubah field yang akan di update, edit pada class serializer.
    """

    model = None
    asset_serializer = None


class BaseUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'premise_detail.html'

    def get(self, request, pk):
        premise = get_object_or_404(self.model, pk=pk)
        serializer = self.asset_serializer(premise)
        return Response({'serializer': serializer, 'premise': premise})


    def post(self, request, pk):
        premise = get_object_or_404(self.model, pk=pk)
        serializer = self.asset_serializer(premise, data=request.data)
        #request.data['modify_by'] = request.user
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'premise': premise})
        serializer.save(modify_by=self.request.user.username)
        next = request.POST.get('next', '/')
        return redirect(next)


class PremiseUpdate(BaseUpdate, UpdateMixin):
    model = Premise
    asset_serializer = PremiseSerializer


class AirValveUpdate(BaseUpdate, UpdateMixin):
    model = AirValve
    asset_serializer = AirValveSerializer


class ValveUpdate(BaseUpdate, UpdateMixin):
    model = Valve
    asset_serializer = ValveSerializer

class PipaUpdate(BaseUpdate, UpdateMixin):
    model = Pipa
    asset_serializer = PipaSerializer

class PumpUpdate(BaseUpdate, UpdateMixin):
    model = Pump
    asset_serializer = PumpSerializer

class PersilUpdate(BaseUpdate, UpdateMixin):
    model = Persil
    asset_serializer = PersilSerializer

    def update(self, instance, request):
        instance.modify_by = request.user
        instance.save()
        return instance

class MeterIndukUpdate(BaseUpdate, UpdateMixin):
    model = MeterInduk
    asset_serializer = MeterIndukSerializer
