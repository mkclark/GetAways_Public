from application import db

class Apartments(db.Model):
    __tablename__ = "apartments"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    # creates the object for the first time
    def __init__(self, name):
        self.name = name

    # 'repr' method prints the data in the terminal
    def __repr__(self):
        return f'<Name {self.name}>'
