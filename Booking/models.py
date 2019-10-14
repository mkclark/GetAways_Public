from application import db

class Apartments(db.Model):
    __tablename__ = "apartments"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Integer, nullable=True)
    image = db.Column(db.String(50), nullable=True)

    # creates the object for the first time
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

    # 'repr' method prints the data in the terminal
    def __repr__(self):
        return f'<Name {self.name}, Price {self.price}>, Image {self.image}'
