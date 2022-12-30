from evapp import db
from evapp.models.model import User

# insert data (update on setup)
db.session.add(User("wcass", "wcass@evapp.com", "change"))
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("evapp", "evapp@evapp.com", "tell"))

# commit the changes
db.session.commit()
