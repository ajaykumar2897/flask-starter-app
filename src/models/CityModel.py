from datetime import datetime
from app import db

class City(db.Model):
   id = db.Column('City',db.Integer,primary_key=True)
   city_name = db.Column(db.Text)
   state_id = db.Column(db.Integer)
   code = db.Column(db.String(15))
   availability_status = db.Column(db.Boolean)
   description = db.Column(db.Text)
   is_default = db.Column(db.Boolean)
   created_at = db.Column(db.DateTime, default=datetime.utcnow)
   updated_at = db.Column(db.DateTime, default=datetime.utcnow)

def __init__(self, city_id,city_name, description, availability_status,is_default,created_at,updated_at):
   self.city_id = id.city_id
   self.city_name = city_name
   self.description = description
   self.availability_status = availability_status
   self.is_default = is_default
   self.created_at = created_at
   self.updated_at = updated_at

def __repr__(self):
    print(self)
    return {}
@property
def serialize(self):
    print(self)
    return {
       'id': self.city_id,
       'city_name': self.city_name,
    }
