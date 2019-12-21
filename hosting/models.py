from application import db

class CreditCards(db.Model):
    __tablename__ = "credit_cards"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    credit_card = db.Column(db.BigInteger(), nullable=True)
    exp_month = db.Column(db.Integer(), nullable=True)
    exp_year = db.Column(db.Integer(), nullable=True)
    security_code= db.Column(db.Integer(), nullable=True)
    address = db.Column(db.String(300), nullable=True)
    address_2 = db.Column(db.String(300), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    postal_code = db.Column(db.Integer(), nullable=True)
    country = db.Column(db.String(100), nullable=True)

    def __init__(self, name, credit_card, exp_month, exp_year, security_code, address, address_2, city, state, postal_code, country):
        self.name = name
        self.credit_card = credit_card
        self.exp_month = exp_month
        self.exp_year = exp_year
        self.security_code = security_code
        self.address = address
        self.address_2 = address_2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    # def __repr__(self):
    #     return f'<Name {self.name}'
