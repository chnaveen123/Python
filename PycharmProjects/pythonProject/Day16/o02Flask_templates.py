
from flask import Flask,render_template,request,session,make_response,redirect,url_for
from datetime import timedelta
app = Flask(__name__)
app.secret_key="HelloWorld"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():
    return render_template("index05.html",uname="Naveen")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for("user",user="user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/users")

def user():
    if "user" in session:
        user = session["user"]
        return f"<h2>welcome {user}</h2>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)

