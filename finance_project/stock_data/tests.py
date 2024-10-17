from stock_data.models import StockPrice

def simple_moving_average_backtest(stock, short_window=50, long_window=200):
    # Get stock prices ordered by date
    prices = StockPrice.objects.filter(stock=stock).order_by('date')
    data = list(prices.values_list('close_price', flat=True))

    short_ma = [sum(data[i:i+short_window])/short_window for i in range(len(data)-short_window)]
    long_ma = [sum(data[i:i+long_window])/long_window for i in range(len(data)-long_window)]

    # Simple crossover backtest logic
    positions = []
    for short, long in zip(short_ma, long_ma):
        if short > long:
            positions.append(1)  # Buy
        else:
            positions.append(-1)  # Sell

    # Calculate performance results
    performance = calculate_performance(data, positions)
    return performance

def calculate_performance(data, positions):
    # This function calculates performance metrics based on positions and price changes
    # Placeholder logic, expand as needed
    return {"profit": sum(positions)}
