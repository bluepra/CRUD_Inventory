from flask import Flask, render_template
import random


# List of inventory entries (dictionaries)
inventory = [
	{"id": 1,
	"item": "Ball",
	"quantity" : 20,
	"price": 3},
	{"id": 2,
	"item": "Jacket",
	"quantity" : 5,
	"price": 60},
	{"id": 3,
	"item": "Table",
	"quantity" : 15,
	"price": 400},
	{"id": 3,
	"item": "Table",
	"quantity" : 15,
	"price": 400}
		 ]


app = Flask(__name__)

# Default page
@app.route('/')  
def home():
	return render_template("index.html", rows = inventory)


if __name__ == "__main__":  
	app.run(debug = True)