from flask import render_template, url_for, redirect, request, flash
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy



app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///ecommerce.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key =True)
    nom = db.Column(db.String(200) ,nullable=False , unique=True)
    email = db.Column(db.String(300), nullable=False , unique=True)
    password = db.Column(db.String(20) ,nullable=False)
db.create_all()

@app.route('/')
def index():
     return render_template("pageaccueil.html")
 
@app.route('/signup', methods = ['GET'])
def signup():
    return render_template("signup.html")

@app.route('/signup', methods = ['POST'])
def signup1():
    if request.method =="POST":
        nom = request.form['nom']
        email = request.form['email']
        password = request.form['password']
        user = User(nom=nom,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
           

@app.route('/login', methods = ['GET'])
def login():
    
    if request.method == 'GET':
        return render_template("login.html")
   
    
    
@app.route('/login', methods = ['POST'])
def login1():
    if request.method =="POST":
        return redirect(url_for('conn'))

@app.route('/connexion')
def conn():
    return render_template("connexion.html")

@app.route('/logout')
def logout():
    return render_template("pageaccueil.html")


if __name__ == '__main__':
    app.run(debug= True)