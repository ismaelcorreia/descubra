from flask import Blueprint, jsonify, request
from model.empresa import Empresa
from connection.connection_alq import db
from util.http_response import httpResponseBody
import uuid

empresa_bp = Blueprint('empresa', __name__)


@empresa_bp.route('/', methods=['GET'])
@empresa_bp.route('/<string:empresa_id>', methods=['GET'])
def find_empresas(empresa_id=None):
    if empresa_id is not None:
        empresa = Empresa.query.get(empresa_id)
        if empresa:
            return httpResponseBody(empresa.to_dict(), 'empresa found', 200)
        else:
            return httpResponseBody(None, 'empresa not found', 404)
    empresas = Empresa.query.all()
    data = []
    for empresa in empresas:
        data.append(empresa.to_dict())
    return httpResponseBody(data, 'list of empresas', 200)


@empresa_bp.route('/', methods=['POST'])
def create_empresa():
    try:
        form_data = request.form.to_dict()
        data = jsonify(form_data).json
        product_id = str(uuid.uuid4())

        empresa = Empresa(
            id=product_id,
            document_number=data['document_number'],
            name=data['name'],
            email=data['email'],
            address=data['address'],
            phone=data['phone']
        )

        db.session.add(empresa)
        db.session.commit()
        empresa = Empresa.query.get(product_id)

        return httpResponseBody(empresa.to_dict(), 'empresa saved!', 200) \
            if empresa else httpResponseBody([], 'canot save the empresa!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@empresa_bp.route('/<string:empresa_id>', methods=['PUT'])
def edit_empresa(empresa_id):
    try:
        empresa = Empresa.query.get(empresa_id)
        if not empresa:
            return httpResponseBody(None, 'empresa not found!', 404)

        form_data = request.form.to_dict()
        data = jsonify(form_data).json

        empresa.name = data['name']
        # empresa.email = data['email']
        empresa.document_number = data['document_number']
        empresa.address = data['address']
        empresa.phone = data['phone']

        db.session.add(empresa)
        db.session.commit()

        return httpResponseBody(empresa.to_dict(), 'empresa edited!', 200)
    except Exception as e:
        # Log the exception or handle it according to your needs
        return httpResponseBody([], f'Error: {str(e)}', 500)


@empresa_bp.route('/<int:empresa_id>', methods=['DELETE'])
def delete_empresa(empresa_id):
    empresa = Empresa.query.get(empresa_id)
    if empresa:
        Empresa.query.get(empresa_id).delete()
        return httpResponseBody(empresa.to_dict(), 'empresa deleted', 200)
    else:
        return httpResponseBody(None, 'empresa not found', 404)

