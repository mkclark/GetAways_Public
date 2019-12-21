from application import db

class Apartments(db.Model):
    __tablename__ = "apartments"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(), nullable=True)
    bedrooms = db.Column(db.Integer, nullable=True)
    baths = db.Column(db.Integer, nullable=True)
    sleeps = db.Column(db.Integer, nullable=True)
    sq_ft = db.Column(db.Integer, nullable=True)
    features = db.relationship('ApartmentFeatures', backref='apartment', lazy='dynamic') # use 'dynamic' on pretty much all the use cases. Check the documentation for more info. It's something about how it loads or something.

    # creates the object for the first time
    def __init__(self, name, price, image, location, bedrooms, baths, sleeps, sq_ft):
        self.name = name
        self.price = price
        self.image = image
        self.location = location
        self.bedrooms = bedrooms
        self.baths = baths
        self.sleeps = sleeps
        self.sq_ft = sq_ft

    # 'repr' method prints the data in the terminal
    def __repr__(self):
        return f'Name {self.name}, Price {self.price}>, Image {self.image}, Location {self.location}, Bedrooms {self.bedrooms}, Baths {self.baths}, Sleeps {self.sleeps}, Square Footage {self.sq_ft}'


class ApartmentFeatures(db.Model):
    __tablename__ = "apartment_features"

    id = db.Column(db.Integer, primary_key=True)
    feature_name = db.Column(db.Text)
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartments.id'))
    category = db.Column(db.Text) # Featured/Safety/General/Kitchen etc.

    def __init__(self, feature_name, apartment_id, category):
        self.feature_name = feature_name
        self.apartment_id = apartment_id
        self.category = category
