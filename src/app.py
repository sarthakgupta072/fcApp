# The main app code goes here

from typing import Collection
from connexion import App
from flask_pymongo import PyMongo

app = App(__name__)

print("Connexion app created")

# Set configurations for connexion app
app.host = '0.0.0.0'
app.port = '8080'
app.debug = True

print("connexion app configured")

# Register MongoDB
app.app.config["MONGO_URI"] = "mongodb://localhost:27017/PG3"

# TODO: Try to remove this later

mongo = PyMongo(app.app)

# db = mongo.db['PG1']

resident = {
    "Room": "102",
    "Name": "Sarthak Gupta",
    "Hometown": "Jammu",
    "Company": "Intuit"
}

collection1id = mongo.db['collection1'].insert_one(resident).inserted_id
print("Database should be created till now")

if __name__ == '__main__':
    app.run()
