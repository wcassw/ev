from evapp import db

# create the database and the db table
db.create_all()

# insert data
# db.session.add()

# commit the changes
db.session.commit()
