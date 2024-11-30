import sqlite3

@app.route('/')
def index():
    return render_tempplate('index.html')

@app.route('/result')
def result:
    connection = sqlite3.connect("database.sqlite")
    cursor = connection.cursor()
    cards = cursor.execute("SELECT * FROM brawlers").fetchall()
    connection.close()
    return render_template('brawlers.html', brawlers=cards)

app.run(debug=True)

