# calculator_engine.py

def run_forecast(portfolio, forecast_months):
    """
    Runs the dividend forecast calculation.
    this function is pure logic: it takes data in and returns results.
    it does not interact with the user

    Args:
        portfolio (list): A list of dictionaries, where each dictionary is a stack.
        forecast_months (int): The Number of months to forecast.

    Returns:
        list: A list of formatted strings representing the monthly results.
    """
    results_log = []

    for month in range(1, forecast_months + 1):
        results_log.append(f"\n---------- Month {month} ----------")
        total_monthly_income = 0

        for stock in portfolio:
            # 1. Calculate Monthly Dividend
            monthly_dividend = stock['shares'] * stock['dividend']
            total_monthly_income += monthly_dividend

            # 2. Calculate New Shares from DRIP (reinvestment)

            reinvested_shares = monthly_dividend / stock['price']

            # add the results for this stock to the log
            results_log.append(f"   {stock['ticker']}:")
            results_log.append(f"   Shares owned: {stock['shares']:.2f}")
            results_log.append(f"   Monthly Income: ${monthly_dividend:.2f}")
            results_log.append(f"   New Shares Purchased (DRIP): {reinvested_shares:.2f}")

            # 3. Update total shares for the next month
            stock['shares'] += reinvested_shares

        results_log.append("---------------------------------")
        results_log.append(f"Total Income for Month {month}: ${total_monthly_income:.2f}")
        results_log.append("=================================")

    return results_log
