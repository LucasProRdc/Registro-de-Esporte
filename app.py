from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)

open("shows.db", "w").close()
db = SQL("sqlite:///shows.db")

db.execute("CREATE TABLE registro (id INTEGER, nome TEXT, esporte TEXT, idade TEXT)")

ESPORTES=["Futebol","Vôlei","Basquete","Ping Pong","Xadrez"
]

@app.route("/")
def index():
   return render_template("index.html", sports=ESPORTES)

@app.route("/consulta", methods=["POST"])
def consulta():
   esporte = request.form.get("esporte")
   nome = request.form.get("nome")
   idade = request.form.get("idade")

   if not nome:
      return render_template("falha.html", mensagem="Campo nome vazio")
   if not idade:
      return render_template("falha.html", mensagem="Campo idade vazio")
   if not esporte:
      return render_template("falha.html", mensagem="Campo esporte vazio")
   if esporte not in ESPORTES:
      return render_template("falha.html", mensagem="Esporte inválido")

   db.execute("INSERT INTO registro (nome, esporte, idade) VALUES(?, ?, ?)", nome, esporte, idade)
   registros = db.execute("SELECT * FROM registro")

   return render_template("registros.html", registros=registros)