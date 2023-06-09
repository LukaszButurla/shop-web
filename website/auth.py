from flask import Blueprint, render_template, request, flash
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        if len(name) < 2 :
            flash("Imie jest zbyt krókie", category="error")
        elif password1 != password2:
            flash("Hasła nie są takie same", category="error")
        elif len(password1) < 7:
            flash("Hasło musi mieć minimum 7 znaków", category="error")
        else:
            new_user = User(email = email, name = name, password = generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            flash("Rejestracja przebiegła pomyślnie", category="success")
    
    return render_template("sign_up.html")

@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                print("login")
            else:
                print("Incorrect password")
        else:
            print("account doesnt exits")
            
    return render_template("login.html")