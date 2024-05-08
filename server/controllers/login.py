from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_pymongo import PyMongo
from ..config import SECRET_KEY, DB_URL

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGO_URI'] = DB_URL

jwt = JWTManager(app)
mongo = PyMongo(app)

@app.route('/login', methods=['POST'])
def login():
    # Authenticate user (example)
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'admin' or password != 'password':
        return jsonify({"msg": "Bad username or password"}), 401

    # Create access token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify({'message': 'protected endpoint'}), 200

if __name__ == '__main__':
    app.run(debug=True)
