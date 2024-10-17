from django.shortcuts import render
from .tests import simple_moving_average_backtest
from stock_data.models import Stock

def report_view(request, ticker):
    stock = Stock.objects.get(ticker=ticker)
    performance = simple_moving_average_backtest(stock)
    
    context = {
        'stock': stock,
        'performance': performance
    }
    return render(request, 'report.html', context)

