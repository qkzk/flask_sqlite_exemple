from flask import Flask, render_template
import sqlite3

query = "SELECT * FROM `exempe`"
app = Flask(__name__)

class Personne:
	def __init__(self, tup: tuple):
		self.__id = tup[0]
		self.__nom = tup[1]

	def format(self):
		return self.__nom

	def __repr__(self):
		return self.format()

@app.route("/")
def index():
	conn = sqlite3.connect("ex.bdd.db")
	curr = conn.cursor()
	curr.execute(query)
	noms = curr.fetchall()
	personnes = [Personne(nom) for nom in noms]
	print(personnes)
	return render_template("index.html", personnes=personnes)

app.run(debug=True, port=8888)