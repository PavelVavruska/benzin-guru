from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from .models import GasStation, GasPrice


def index(request):
    gas_station_list = GasStation.objects.all()
    context = {'gas_station_list': gas_station_list}
    return render(request, 'fuel/index.html', context)


def detail(request, gas_station_id):
    gas_station = get_object_or_404(GasStation, pk=gas_station_id)
    return render(request, 'fuel/detail.html', {'gas_station': gas_station})
