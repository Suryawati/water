from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from water.models import Premise, MeterInduk, Pump, AirValve, Pipa
from django.db.models import Count, Sum
import json


class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'main_05200953.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

       #Pelanggan
        query1 = Premise.objects.all().values('status').annotate(total=(Count('*')))
        # data = Premise.objects.all()
        data1 = json.dumps(list(query1)) #.replace('\ ',' ')
        context['statuspel'] = data1

        query2 = Premise.objects.all().values('premise_type').annotate(total=(Count('*')))
        data2 = json.dumps(list(query2))
        context['typepel'] = data2

        query3 = Premise.objects.all().values('kode_gol').annotate(total=(Count('*')))
        data3 = json.dumps(list(query3))
        context['golpel'] = data3

        #Meter Induk
        query4 = MeterInduk.objects.all().values('status').annotate(total=(Count('*')))
        data4 = json.dumps(list(query4))
        context['meter'] = data4

        # Pump
        query5 = Pump.objects.all().values('tipe').annotate(total=(Count('*')))
        data5 = json.dumps(list(query5))
        context['pump'] = data5

        # Air Valve
        query6 = AirValve.objects.all().values('merek').annotate(total=(Count('*')))
        data6 = json.dumps(list(query6))
        context['avalve'] = data6

        # Pipa
        query7 = Pipa.objects.all().values('material_pipa').annotate(total=(Sum('pjg_pipa_geometris')))
        # data = Premise.objects.all()
        data7 = json.dumps(list(query7))
        context['materialpipa'] = data7

        query8 = Pipa.objects.all().values('kelas_pipa').annotate(total=(Sum('pjg_pipa_geometris')))
        data8 = json.dumps(list(query8))
        context['kelaspipa'] = data8

        query9 = Pipa.objects.all().values('status').annotate(total=(Sum('pjg_pipa_geometris')))
        data9 = json.dumps(list(query9))
        context['statuspipa'] = data9

        return context

