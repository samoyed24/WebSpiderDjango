from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from gdpview.spider import GdpSpider
from gdpview.models import *
from gdpview.charts import mapCharts


@require_http_methods(['POST'])
def update_data(request):
    data = GdpSpider.get_latest_data()
    for _ in data:
        GDPdata.objects.update_or_create(
            region_name=_['region_name'],
            year=_['year'],
            type=_['type'],
            value=_['value']
        )
    nation_data = GdpSpider.getNationalData()
    for _ in nation_data:
        NationalData.objects.update_or_create(
            year=_['year'],
            type=_['type'],
            value=_['value']
        )
    return JsonResponse({'success': True, 'code': '20000', 'msg': 'OK'})


def get_gdp_data(request):
    map_embed = mapCharts.fetch_data()
    return HttpResponse(map_embed)


def index(request):
    return render(request, 'index.html')
