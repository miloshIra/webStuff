import json

from flask import Blueprint, render_template, request, redirect, url_for

from models.stores.store import Store

store_blueprint = Blueprint('stores',__name__)

@store_blueprint.route('/')
def index():
    return "This is the store index"

@store_blueprint.route('/store/<string:name>')
def store_page():
    pass
