from flask_wtf import FlaskForm
from wtforms import validators, StringField, IntegerField, SubmitField

class PaymentForm(FlaskForm):
    name = StringField('name', [validators.InputRequired()])
    credit_card = IntegerField('credit_card', [validators.InputRequired()])
    exp_month = IntegerField('exp_month', [validators.InputRequired()])
    exp_year = IntegerField('exp_year', [validators.InputRequired()])
    security_code = IntegerField('security_code', [validators.InputRequired()])
    address = StringField('address', [validators.InputRequired()])
    address_2 = StringField('address_2')
    city = StringField('city', [validators.InputRequired()])
    state = StringField('state', [validators.InputRequired()])
    postal_code = IntegerField('postal_code', [validators.InputRequired()])
    state = StringField('state', [validators.InputRequired()])
