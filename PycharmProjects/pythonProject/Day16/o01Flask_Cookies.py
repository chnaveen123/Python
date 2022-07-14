
from flask import Flask,render_template,request, make_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index05.html",uname="Naveen")

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("Success")
    resp.set_cookie("Prod1","Pepsi")
    resp.set_cookie("Prod2","Tropicana")
    return resp

@app.route("/get_cookie")
def get_cookie():
    prd1 = request.cookies.get("Prod1")
    prd2 = request.cookies.get("Prod2")
    if prd1 == None:
        prd1 = "Cookie Deleted"
    elif prd2 == None:
        prd2 = "Cookie Deleted"
    return "<h2> First Cookie :" + prd1 + "<br>  Second Cookie :"+prd2+"</h2>"

@app.route("/del_cookie")
def del_cookie():
    resp = make_response("Deleted Cookie Successfuly")
    resp.delete_cookie(("Prod2"))
    return resp





if __name__ == "__main__":
    app.run(debug=True)


