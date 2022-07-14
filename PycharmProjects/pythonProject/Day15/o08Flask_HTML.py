
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")

def home():
    return render_template("index05.html", uname="MOhammed Ali")

if __name__ == "__main__":
    app.run(debug=True)