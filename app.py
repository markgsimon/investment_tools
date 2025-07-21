# app.py
from flask import Flask, render_template, request, redirect, url_for, session
from calculator_engine import run_forecast # Import our existing engine
import os #Import the os module to access environment variables
from dotenv import load_dotenv # import the function to load the .env file

# Load envrionment variables from .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# A secret key is needed to securely manage session data
# It's loaded from an envrionment variable for security
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
