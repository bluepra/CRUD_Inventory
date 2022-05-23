# This file is meant to be run ONCE to create the .db file

from app import db
from app import Item, Warehouse

db.create_all()