from django.core.management.base import BaseCommand
import requests
from stock_data.models import Stock, StockPrice
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch financial data from API'

    def handle(self, *args, **kwargs):
        # Sample API call (adjust for your API of choice)
        api_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=YU19NYRQHV552HW9"
        response = requests.get(api_url).json()

        stock, _ = Stock.objects.get_or_create(ticker="IBM", name="IBM Corporation")

        # Parsing the API response and saving data
        for date_str, daily_data in response['Time Series (Daily)'].items():
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            StockPrice.objects.update_or_create(
                stock=stock,
                date=date,
                defaults={
                    'open_price': daily_data['1. open'],
                    'close_price': daily_data['4. close'],
                    'high': daily_data['2. high'],
                    'low': daily_data['3. low'],
                    'volume': daily_data['5. volume']
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully fetched data'))
