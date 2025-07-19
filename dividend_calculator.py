# dividend_calculator.py

def get_float_input(prompt):
    """A helpter function to get a valid non-negative float from the user."""
    while True:
        try:
            # Get input and remove any comas
            value_str = input(prompt).replace(',','')
            value = float(value_str)
            if value >= 0:
                return value
            else:
                print("Input annot be negative. Please enter a positive number or zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number (e.g., 10.50 or 20,000.")

def get_int_input(prompt):
    """A helper function to get a valid positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def forecast_dividends():
    """
    Calculates and forecasts compounding dividend income for a user-defined portfolio and a user-defined forecast period.
    :return:
    """
    # ---Greeting---
    print("Welcome to the Dividend Forecast Calculator!")
    print("=" * 40)

# --- User Input & Portfolio Creation ---
    portfolio = []

    while True:
        print("\n--- Adding a New Stock to Your Portfolio ---")

        # 1. Get Ticker
        ticker = input("Enter the stock ticker (e.g., AAPL): ").upper()

        # 2. Get Stock Price
        price = get_float_input(f"Enter the current price for {ticker}: $")
        if price == 0:
            print("Stock price cannot be zero. Please re-enter the stock")
            continue

        # 3. Get Dividend Per Share
        dividend_per_share = get_float_input(f"Enter the monthly dividend per share for {ticker}: $")

        # 4. Get Initial Investment
        initial_investment = get_float_input(f"Enter your initial investment for {ticker}: $")

        # Calculate initial number of shares
        initial_shares = initial_investment / price
        # Store all data for this stock in a dictionary
        stock_info = {
            'ticker': ticker,
            'price': price,
            'dividend': dividend_per_share,
            'shares': initial_shares,
        }

        # Add the stock to our portfolio list
        portfolio.append(stock_info)
        print(f"Successfully {ticker} to your portfolio.")

        # Ask user if they want to add another stock
        add_another = input("Do you want to add another stock? (y/n): ").lower()
        if add_another != 'y':
            break

    if not portfolio:
        print("\nNo stocks were added to the portfolio. Exiting program.")
        return

    # --- Get Forecast Duration ---
    print("\n" + "=" * 40)
    forecast_months = get_int_input("How many months would you like to forecast? ")
    print("=" * 40)


# --- Run the program ---
if __name__ == "__main__":
    forecast_dividends()

