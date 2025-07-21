# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from calculator_engine import run_forecast # Import our existing engine
import os #Import the os module to access environment variables
from dotenv import load_dotenv # import the function to load the .env file

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# A secret key is needed to securely manage session data
# It's loaded from an environment variable for security
# The second argument is a default key for safety if the variable isn't set.
app.secret_key = os.getenv('SECRET_KEY', 'a_default_fallback_key_for_development')

@app.route('/')
def index():
    """
    This is the main route. it displays the form to add stocks and shows the current portfolio stores in the session. and shows the current portfolio stores in the session
    """
    # 'session' is a dictionary that stores data for a user across requests.
    # we initialize an empty portfolio list if it doesn't exist.
    if 'portfolio' not in session:
        session['portfolio'] = []
    return render_template('index.html', portfolio=session['portfolio'])

@app.route('/add_stock', methods=['POST'])
def add_stock():
    """
    This route handles the form submission for adding a new stock. It processes the form data and adds the new stock to the session profile
    """
    try:
        # Get data from the submitted form
        ticker = request.form['ticker'].upper()
        price = float(request.form['price'])
        dividend = float(request.form['dividend'])
        investment = float(request.form['investment'])

        if price == 0:
            # in production, we will show an error message. for now, we just won't add it.
            return redirect(url_for('index'))

        # Calculate initial shares
        initial_shares = investment / price

        # Create the stock dictionary
        stock_info = {
            'ticker': ticker,
            'price': price,
            'dividend': dividend,
            'shares': initial_shares,
        }

        # Add the new stock to the portfolio in the session
        session['portfolio'].append(stock_info)
        # session.modified = True is needed to tell Flask the session has changed
        session.modified = True

    except (ValueError, KeyError) as e:
        # basic error handling if form data is bad
        print(f"Error processing form: {e}")
    # Redirect the user back to the main page
    return redirect(url_for('index'))

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    This route handles the forecast calculation. It gets the portfolio from the session, calls the engine, and displays the results.
    :return:
    """
    try:
        forecast_months = int(request.form['months'])
        portfolio = session.get('portfolio', [])

        if not portfolio or forecast_months <= 0:
            return redirect(url_for('index'))

        # call our reliable engine to do the heavy lifting
        results_log = run_forecast(portfolio, forecast_months)

        # Render the results page, passing the log to it
        return render_template('results.html', results=results_log)

    except (ValueError, KeyError) as e:
        print(f"Error during calculation: {e}")
        return redirect(url_for('index'))

@app.route('/clear')
def clear_session():
    """
    A simple route to clear the session and start over
    :return:
    """
    session.clear()
    return redirect(url_for('index'))

# This allows the script to be run directly
if __name__ == '__main__':
    # 'debug=True' makes development easier. It auto-reloads when you save changes.
    app.run(debug=True)
