
import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars
from flask_pymongo import PyMongo



app = Flask(__name__)


# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.mars_db
collection = db.mars_facts






@app.route('/scrape')
def scrape():
   
    ma = scrape_mars.scrape()
    db.mars_facts.insert_one(ma)
    return "Some scrapped data"


@app.route("/")
def home():

    mars = list(db.mars_facts.find())
    
    return render_template("index.html", mars = mars)


if __name__ == "__main__":
    app.run(debug=True)
