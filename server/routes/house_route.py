import os

from flask import Blueprint, jsonify, request
from model.house import House
from connection.connection_alq import db
from util.http_response import httpResponseBody
from service.upload_service import upload_file
import uuid

house_bp = Blueprint('house', __name__)


@house_bp.route('/', methods=['GET'])
@house_bp.route('/<string:house_id>', methods=['GET'])
def find_houses(house_id=None):
    if house_id is not None:
        house = House.query.get(house_id)
        if house:
            return httpResponseBody(house.to_dict(), 'house found', 200)
        else:
            return httpResponseBody(None, 'house not found', 404)
    houses = House.query.all()
    data = []
    for house in houses:
        data.append(house.to_dict())
    return httpResponseBody(data, 'list of houses', 200)


@house_bp.route('/by-category/<string:category_id>', methods=['GET'])
def find_houses_by_categories(category_id=None):
    # if category_id is not None:
    houses = House.query.filter_by(category_id=category_id).all()
    data = []
    for house in houses:
        data.append(house.to_dict())
    return httpResponseBody(data, 'list of houses', 200)


@house_bp.route('/', methods=['POST'])
def create_house():
    try:
        form_data = request.form.to_dict()
        data = jsonify(form_data).json
        house_id = str(uuid.uuid4())

        data['url_img'] = os.environ.get("BASE_URL_PHOTOS") + "default.jpg"
        files = request.files
        if files:
            file_save = upload_file(files, filename=house_id, property_name='image')
            data['url_img'] = f"{os.environ.get("BASE_URL_PHOTOS") + os.path.basename(file_save[0])}"

        house = House(
            id=house_id,
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category_id=data['category_id'],
            url_img=data['url_img'],
            source_id=data.get('source_id')
        )

        if data.get("tax_vat"):
            house.tax_vat = data["tax_vat"]

        db.session.add(house)
        db.session.commit()
        house = House.query.get(house_id)

        return httpResponseBody(house.to_dict(), 'house saved!', 200) \
            if house else httpResponseBody([], 'canot save the house!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@house_bp.route('/<string:house_id>', methods=['PUT'])
def edit_house(house_id):
    try:
        house = House.query.get(house_id)
        if house is None:
            return httpResponseBody(None, 'house not found', 404)

        form_data = request.form.to_dict()
        data = jsonify(form_data).json

        data['url_img'] = os.environ.get("BASE_URL_PHOTOS") + "default.jpg"
        files = request.files
        if files:
            # file_save = upload_file(files, folder_name='houses', filename=house_id, property_name='image')
            file_save = upload_file(files, filename=house_id, property_name='image')
            data['url_img'] = f"{os.environ.get("BASE_URL_PHOTOS") + os.path.basename(file_save[0])}"

        house.name = data['name']
        house.description = data['description']
        house.price = data['price']
        house.category_id = data['category_id']
        house.url_img = data['url_img']
        house.source_id = data.get('source_id')

        # if data.get("tax_vat"):
        #     house.tax_vat = data["tax_vat"]

        db.session.add(house)
        db.session.commit()
        house = House.query.get(house_id)

        return httpResponseBody(house.to_dict(), 'house edited!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@house_bp.route('/<string:house_id>', methods=['DELETE'])
def delete_house(house_id):
    house = House.query.get(house_id)
    if house:
        db.session.delete(house)
        db.session.commit()
        # House.query.get(house_id).delete()
        return httpResponseBody({}, 'house deleted', 200)
    else:
        return httpResponseBody(None, 'house not found', 404)
