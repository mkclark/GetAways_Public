from flask import Blueprint, render_template

booking_app = Blueprint('booking_app', __name__)

@booking_app.route('/')
def index():
    return render_template('booking.html')

@booking_app.route('/search_results')
def search_results():
    return render_template('search_results.html')
