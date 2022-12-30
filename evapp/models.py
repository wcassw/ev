from evapp import db
from evapp import bcrypt

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Vehicle(Base):
    __tablename__ = "vehicle"

    evid = Column("evid", Integer, primary_key=True)
    make = Column("make", String, primary_key=True)
    name = Column("name", String)
    price = Column("price", Integer)
    battery = Column("battery", Float)
    evrange  = Column("evrange", Integer)
    evrange_real = Column("evrange_real", Integer)

    def __init__(self, evid, make, name, price, battery, evrange, evrange_real):
        self.evid = evid
        self.make = make
        self.name = name
        self.price = price
        self.battery = battery
        self.evrange= evrange
        self.evrange_real = evrange_real

    def __repr__(self):
        #r_price = locale.currency(self.price, grouping=True, symbol=True)
        return f"({self.make}) {self.name}\n\t\t€{self.price:,.2f}\n\t\tUseable battery: {self.battery:.2f}kWh\n\t\tRange: {self.evrange} km Real: {self.evrange_real} km\n"



class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<name - {}>'.format(self.name)


class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'))

    def __init__(self, title, description, author_id):
        self.title = title
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        return '<title {}'.format(self.title)
