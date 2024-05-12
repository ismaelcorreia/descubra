from flask import Blueprint, jsonify, request
from model.user import User
from model.type_user import TypeUser
from connection.connection_alq import db
from util.http_response import httpResponseBody
import uuid

user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['GET'])
@user_bp.route('/<string:user_id>', methods=['GET'])
def find_users(user_id=None):
    if user_id is not None:
        user = User.query.get(user_id)
        if user:
            return httpResponseBody(user.to_dict(), 'user found', 200)
        else:
            return httpResponseBody(None, 'user not found', 404)
    users = User.query.all()
    data = []
    for user in users:
        data.append(user.to_dict())
    return httpResponseBody(data, 'list of users', 200)


@user_bp.route('/', methods=['POST'])
def create_user():
    try:
        form_data = request.form.to_dict()
        data = jsonify(form_data).json
        product_id = str(uuid.uuid4())

        user = User(
            id=product_id,
            username=data['username'],
            email=data['email'],
            document_number=data['document_number'],
            password=data['password'],
            type_user=TypeUser[data['type_user']],
            name=data['name'],
            address=data['address'],
            phone=data['phone']
        )

        db.session.add(user)
        db.session.commit()
        user = User.query.get(product_id)

        return httpResponseBody(user.to_dict(), 'user saved!', 200) \
            if user else httpResponseBody([], 'canot save the user!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@user_bp.route('/<string:user_id>', methods=['PUT'])
def edit_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return httpResponseBody(None, 'user not found!', 404)

        form_data = request.form.to_dict()
        data = jsonify(form_data).json

        # user.username = data['username']
        # user.email = data['email']
        user.document_number = data['document_number']
        user.password = data['password']
        user.type_user = TypeUser[data['type_user']]
        user.name = data['name']
        user.address = data['address']
        user.phone = data['phone']

        db.session.add(user)
        db.session.commit()

        return httpResponseBody(user.to_dict(), 'user edited!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user:
        User.query.get(user_id).delete()
        return httpResponseBody(user.to_dict(), 'user deleted', 200)
    else:
        return httpResponseBody(None, 'user not found', 404)


@user_bp.route('/login', methods=['POST'])
def login_user():
    form = request.form.to_dict()
    data = jsonify(form).json
    if (data.get("username") and data.get("password")) is not None:
        user = User.query.filter_by(username=data["username"], password=data["password"]).first()

        return httpResponseBody(user.to_dict(), 'user found, logged in!', 201) \
            if user is not None \
            else httpResponseBody(None, 'user not found, username or password is wrong!', 404)

    return httpResponseBody(None, 'missing data, type/fill or fields!', 200)
