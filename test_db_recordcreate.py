from application import create_app
from booking.models import Apartments, ApartmentFeatures
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
app = create_app()
Migrate(app,db)



# creating an apartments
cancun_apartment = Apartments('OCEANFRONT - CASA MAYA PLAYA - BEST LOCATION IN THE FABULOUS HOTEL ZONE', '383', 'Casatotalmente.webp', 'Cancun', '2', '2', '3', '700')

# adding the new apartment to the database
db.session.add_all(cancun_apartment)
db.session.commit()
