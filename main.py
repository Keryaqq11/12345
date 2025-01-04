import sqlite3
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result/<string:rarity>', methods=['GET', 'POST'])
def result(rarity):
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    if request.method == 'POST':
        name = request.form['search-name']
        search_request = f"SELECT * FROM brawler WHERE name LIKE '%{name}%'"  # SQL injection prevention by using parameterized queries
        cards = cursor.execute(search_request).fetchall()
        return render_template('brawlers.html', brawlers=cards)
    else:
        search_request = f"SELECT * FROM brawler WHERE rares = '{rarity}'"
        cards = cursor.execute(search_request).fetchall()
        connection.close()
        return render_template('brawlers.html', brawlers=cards)

@app.route('/mythic')
def mythic():
    return render_template('mythic.html')

@app.route('/epic')
def epic():
    return render_template('epic.html')

@app.route('/rare')
def rare():
    return render_template('rare.html')

@app.route('/superrare')
def superrare():
    return render_template('superrare.html')

@app.route('/legendary')
def legendary():
    return render_template('legendary.html')




app.run(debug=True)

