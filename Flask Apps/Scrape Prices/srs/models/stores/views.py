from flask import Blueprint

store_blueprint('stores',__name__)

@store_blueprint.route('/store/<string:name>')
def store_page():
