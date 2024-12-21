import sqlite3
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM brawlers").fetchall()
    connection.close()
    return render_template('brawlers.html', brawlers=cards)

@app.route('/mythic')
def mythic():
    return render_template('mythic.html')

@app.route('/epic')
def epic():
    return render_template('epic.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/rare')
def rare():
    return render_template('rare.html')

@app.route('/superrare')
def Shelly():
    return render_template('superrare.html')

@app.route('/legendary')
def Shelly():
    return render_template('legendary.html')




app.run(debug=True)

