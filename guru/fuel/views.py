from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import GasStation, GasPrice
from .forms import GasPriceForm


def index(request, *args, **kwargs):
    gas_station_list = GasStation.objects.all()
    context = {'gas_station_list': gas_station_list}
    return render(request, 'fuel/index.html', context)


def detail(request, gas_station_id):
    gas_station = get_object_or_404(GasStation, pk=gas_station_id)
    gas_prices = GasPrice.objects.filter(station=gas_station).order_by('-date')
    form = GasPriceForm
    if gas_prices:
        gas_prices_js = gas_prices[0].price  # newest gas price for this gas station
    else:
        gas_prices_js = ' - Sorry, no gas prices are available.'

    if request.method == 'POST':
        form = GasPriceForm(request.POST)
        if form.is_valid():
            station = form.cleaned_data['station']
            date = form.cleaned_data['date']
            price = form.cleaned_data['price']
            new_gas_price = GasPrice(station=station, date=date, price=price)
            new_gas_price.save()
            user_message = 'Your gas price (%s, %s) was added, thank you for support!' % (station.name, date)
            messages.add_message(request, messages.INFO, user_message)
            return redirect('index')
    else:
        form = GasPriceForm(initial={'station': gas_station, })
    return render(request, 'fuel/detail.html', {'gas_station': gas_station,
                                                'gas_prices': gas_prices,
                                                'gas_prices_js': gas_prices_js,
                                                'form': form})