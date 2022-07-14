
from flask import Flask, render_template
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
        return {"Message": "Hello World"}

api.add_resource(Helloworld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)







