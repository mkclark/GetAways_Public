from flask import Blueprint, render_template, session, url_for, request

from application import db
from booking.models import Apartments, ApartmentFeatures
from booking.forms import SearchForm

booking_app = Blueprint('booking_app', __name__)

@booking_app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    search_input = request.args.get('search_input')

    apartments = db.session.query(Apartments.name, Apartments.price, Apartments.image).order_by(Apartments.id).all()

######

    # # creating an apartments
    # cancun_apartment = Apartments('OCEANFRONT - CASA MAYA PLAYA - BEST LOCATION IN THE FABULOUS HOTEL ZONE', '383', 'Casatotalmente.webp', 'Cancun', '2', '2', '3', '700')
    #
    # # adding the new apartment to the database
    # db.session.add(cancun_apartment)
    # db.session.commit()
    #
    # # creating features for the apartment
    #
    # cancun_apartment_feature1 = ApartmentFeatures('Children Welcome', cancun_apartment.id, 'Featured')
    # cancun_apartment_feature2 = ApartmentFeatures('TV', cancun_apartment.id, 'Featured')
    #
    # db.session.add_all([cancun_apartment_feature1, cancun_apartment_feature2])
    # db.session.commit()

#######


    return render_template('booking.html', apartments=apartments)


@booking_app.route('/search_results')
def search_results():

    location = request.args.get('search_input')

    search_result_apartments = db.session.query(Apartments.name, Apartments.price, Apartments.image, Apartments.baths, Apartments.bedrooms, Apartments.sleeps, Apartments.sq_ft).order_by(Apartments.id).filter(Apartments.location == location)

    return render_template('search_results.html', apartments=search_result_apartments, location=location)


@booking_app.route('/search_details', methods=['GET', 'POST'])
def search_details():

    apartment = db.session.query(Apartments.name, Apartments.price, Apartments.image, Apartments.baths, Apartments.bedrooms, Apartments.sleeps).filter(Apartments.id == '12')
    apartment_details_featured = db.session.query(ApartmentFeatures.feature_name).order_by(ApartmentFeatures.id).filter(ApartmentFeatures.apartment_id == '12', ApartmentFeatures.category == 'Featured')
    apartment_details_safety_features = db.session.query(ApartmentFeatures.feature_name).order_by(ApartmentFeatures.id).filter(ApartmentFeatures.apartment_id == '12', ApartmentFeatures.category == 'Safety Features')
    apartment_details_general = db.session.query(ApartmentFeatures.feature_name).order_by(ApartmentFeatures.id).filter(ApartmentFeatures.apartment_id == '12', ApartmentFeatures.category == 'General')


    return render_template('search_details.html', apartment=apartment, apartment_details_featured=apartment_details_featured)
