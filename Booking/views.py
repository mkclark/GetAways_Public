from flask import Blueprint, render_template

booking_app = Blueprint('booking_app', __name__)

@booking_app.route('/')
def index():
    return render_template('booking.html')
