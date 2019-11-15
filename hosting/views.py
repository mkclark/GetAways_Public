from flask import Blueprint, render_template, session, url_for, request

from application import db

hosting_app = Blueprint('hosting_app', __name__)

@hosting_app.route('/hosting', methods=['GET', 'POST'])
def hosting_home():
    return render_template('hosting_home.html')
