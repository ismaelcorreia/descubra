import os

from flask import Blueprint, jsonify, request
from model.product import Product
from connection.connection_alq import db
from util.http_response import httpResponseBody
from service.upload_service import upload_file
import uuid

product_bp = Blueprint('product', __name__)


@product_bp.route('/', methods=['GET'])
@product_bp.route('/<string:product_id>', methods=['GET'])
def find_products(product_id=None):
    if product_id is not None:
        product = Product.query.get(product_id)
        if product:
            return httpResponseBody(product.to_dict(), 'product found', 200)
        else:
            return httpResponseBody(None, 'product not found', 404)
    products = Product.query.all()
    data = []
    for product in products:
        data.append(product.to_dict())
    return httpResponseBody(data, 'list of products', 200)


@product_bp.route('/by-category/<string:category_id>', methods=['GET'])
def find_products_by_categories(category_id=None):
    # if category_id is not None:
    products = Product.query.filter_by(category_id=category_id).all()
    data = []
    for product in products:
        data.append(product.to_dict())
    return httpResponseBody(data, 'list of products', 200)


@product_bp.route('/', methods=['POST'])
def create_product():
    try:
        form_data = request.form.to_dict()
        data = jsonify(form_data).json
        product_id = str(uuid.uuid4())

        data['url_img'] = os.environ.get("BASE_URL_PHOTOS") + "default.jpg"
        files = request.files
        if files:
            file_save = upload_file(files, filename=product_id, property_name='image')
            data['url_img'] = f"{os.environ.get("BASE_URL_PHOTOS") + os.path.basename(file_save[0])}"

        product = Product(
            id=product_id,
            name=data['name'],
            description=data['description'],
            price=data['price'],
            category_id=data['category_id'],
            url_img=data['url_img'],
            source_id=data.get('source_id')
        )

        if data.get("tax_vat"):
            product.tax_vat = data["tax_vat"]

        db.session.add(product)
        db.session.commit()
        product = Product.query.get(product_id)

        return httpResponseBody(product.to_dict(), 'product saved!', 200) \
            if product else httpResponseBody([], 'canot save the product!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@product_bp.route('/<string:product_id>', methods=['PUT'])
def edit_product(product_id):
    try:
        product = Product.query.get(product_id)
        if product is None:
            return httpResponseBody(None, 'product not found', 404)

        form_data = request.form.to_dict()
        data = jsonify(form_data).json

        data['url_img'] = os.environ.get("BASE_URL_PHOTOS") + "default.jpg"
        files = request.files
        if files:
            # file_save = upload_file(files, folder_name='products', filename=product_id, property_name='image')
            file_save = upload_file(files, filename=product_id, property_name='image')
            data['url_img'] = f"{os.environ.get("BASE_URL_PHOTOS") + os.path.basename(file_save[0])}"

        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.category_id = data['category_id']
        product.url_img = data['url_img']
        product.source_id = data.get('source_id')

        # if data.get("tax_vat"):
        #     product.tax_vat = data["tax_vat"]

        db.session.add(product)
        db.session.commit()
        product = Product.query.get(product_id)

        return httpResponseBody(product.to_dict(), 'product edited!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@product_bp.route('/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        # Product.query.get(product_id).delete()
        return httpResponseBody({}, 'product deleted', 200)
    else:
        return httpResponseBody(None, 'product not found', 404)
