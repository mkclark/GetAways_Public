from flask import Blueprint, render_template

from application import db
from booking.models import Apartments

booking_app = Blueprint('booking_app', __name__)

@booking_app.route('/')
def index():
    apartments = Apartments("Cancun Apartment 1")
    db.session.add(apartments)
    db.session.commit()

    return render_template('booking.html')

@booking_app.route('/search_results')
def search_results():
    return render_template('search_results.html')

@booking_app.route('/search_details')
def search_details():
    return render_template('search_details.html')
