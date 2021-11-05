from django.shortcuts import render

from base.bitcoin import convert_brl_btc


def home(request):
    btc_price = convert_brl_btc(1000)
    context = {
        'btc_price': btc_price,
    }
    return render(request, 'base/home.html', context)
