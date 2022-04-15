#!/usr/bin/python3
"""
app_views; Blueprint instance
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__)
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.amenities import *
