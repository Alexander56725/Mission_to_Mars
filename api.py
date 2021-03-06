
#use Flask and Mongo to begin creating Robin's web app
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#set up Flask:
app = Flask(__name__)

# How to connect to Mongo using PyMongo.
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#linking
@app.route("/") 
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars) 


#set up scarping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_many({}, {"$set": mars_data}, upsert=True)
   return redirect('/', code=302)

#Flask run
if __name__ == "__main__":
   app.run()