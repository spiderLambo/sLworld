try:
    from secret.hash import hash
except ImportError:
    from public.hash import hash
from flask import Flask, render_template, request, redirect
from databases.controler.user import *
import regex_verif


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("connected.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if connected(username, hash(request.form.get("password"), username)):
            return redirect('/')
    return render_template("connexion.html")

@app.route('/register',  methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        displayName = request.form.get('displayName')
        email = request.form.get('email')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')
        if (
            not regex_verif.username(username) or
            not regex_verif.email(email) or
            password != confirmPassword or
            not regex_verif.passworld(password) or
            username_used(username)
        ):
            return render_template("badRegister.html")
        else:
            add_user(username, displayName, hash(password, username), email)
            return redirect('/login')
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)