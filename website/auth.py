from flask import Blueprint, render_template, request

auth = Blueprint("auth", __name__)

@auth.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        print(email, name, password1, password2)
    
    
    return render_template("sign_up.html")