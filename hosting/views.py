from flask import Blueprint, render_template, session, url_for, request

from application import db
from hosting.models import CreditCards
from hosting.forms import PaymentForm


hosting_app = Blueprint('hosting_app', __name__)

@hosting_app.route('/hosting', methods=['GET', 'POST'])
def hosting():
    form = PaymentForm()

    credit_card = CreditCards(
        form.name.data,
        form.credit_card.data,
        form.exp_month.data,
        form.exp_year.data,
        form.security_code.data,
        form.address.data,
        form.address_2.data,
        form.city.data,
        form.state.data,
        form.postal_code.data,
        form.state.data
    )
    db.session.add(credit_card)
    db.session.commit()

    return render_template('hosting_home.html', form=form)

@hosting_app.route('/hosting_checklist')
def hosting_checklist():
    return render_template('hosting_location.html')
