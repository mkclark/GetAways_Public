from flask import Blueprint, render_template

from application import db
from booking.models import Apartments

booking_app = Blueprint('booking_app', __name__)

@booking_app.route('/')
def index():

    # db.session.query(Apartments).filter(Apartments.image == None)
    # db.update({apartments.image: "no image"}, synchronize_session = False)


    apartments = db.session.query(Apartments.name, Apartments.price, Apartments.image).order_by(Apartments.id).all()

    return render_template('booking.html', apartments=apartments)

@booking_app.route('/search_results')
def search_results():
    return render_template('search_results.html')

@booking_app.route('/search_details')
def search_details():
    return render_template('search_details.html')
