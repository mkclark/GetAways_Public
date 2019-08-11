from flask import Blueprint

booking_app = Blueprint('booking_app', __name__)

@booking_app.route('/')
def index():
    return 'Booking Home'
