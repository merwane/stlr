from flask import Flask
from flask_restful import Api
from flask_cors import CORS

# methods
from controllers.send import GenerateAccount, SendTx, Claim, SendClaim

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}})

api = Api(app)

# routes
api.add_resource(GenerateAccount, "/api/gen/<string:phone>")
api.add_resource(SendTx, "/api/send/<string:uid>")
api.add_resource(Claim, "/api/claim/<string:uid>")
api.add_resource(SendClaim, "/api/sendclaim/<string:uid>")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
