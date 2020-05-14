from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# methods


app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)

# routes


if __name__ == '__main__':
    app.run(port=5000)
