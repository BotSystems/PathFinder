from models import Chanel, db

# Connect to our database.
db.connect()

# Create the tables.
db.create_tables([Chanel])
