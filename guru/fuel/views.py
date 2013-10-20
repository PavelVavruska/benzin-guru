from django.shortcuts import get_object_or_404, render
from .models import GasStation, GasPrice


def index(request):
    gas_station_list = GasStation.objects.all()
    context = {'gas_station_list': gas_station_list}
    return render(request, 'fuel/index.html', context)


def detail(request, gas_station_id):
    gas_station = get_object_or_404(GasStation, pk=gas_station_id)
    gas_prices = GasPrice.objects.filter(station=gas_station).order_by('-date')
    if gas_prices:
        gas_prices_js = gas_prices[0].price  # newest gas price for this gas station
    else:
        gas_prices_js = ' - Sorry, no gas prices are available.'
    return render(request, 'fuel/detail.html', {'gas_station': gas_station,
                                                'gas_prices': gas_prices,
                                                'gas_prices_js': gas_prices_js})
