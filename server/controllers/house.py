from flask import Flask, jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from flask_pymongo import PyMongo
from bson import ObjectId

# from config.static import DB_URL

app = Flask(__name__,
            static_folder='../static',)

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MONGO_URI'] = "mongodb://admin:admin@localhost:27017/db_descubra"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



mongo = PyMongo(app)
# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Create
@app.route('/houses', methods=['POST'])
def add_place():
    data = request.form.to_dict()
    files = request.files.getlist('images')
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            data.setdefault('images', []).append(filename)

    mongo.db.places.insert_one(data)
    return jsonify({'message': 'Place added successfully'}), 201


@app.route('/houses', methods=['GET'])
def get_places():
    places = list(mongo.db.places.find({}, {'_id': 0}))
    return jsonify({'places': places}), 200





# @app.route('/companies', methods=['POST'])
# def add_company():
#     data = request.json
#     company_id = mongo.db.companies.insert_one(data).inserted_id
#     return jsonify({'message': 'Company added successfully', 'id': str(company_id)}), 201


@app.route('/companies', methods=['POST'])
def add_company():
    data = request.form.to_dict()
    file = request.files.get('brand_image')
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data['brand_image'] = filename

    company_id = mongo.db.companies.insert_one(data).inserted_id
    return jsonify({'message': 'Company added successfully', 'id': str(company_id)}), 201


@app.route('/companies', methods=['GET'])
def get_companies():
    companies = list(mongo.db.companies.find({}, {'_id': 0}))
    return jsonify({'companies': companies}), 200

@app.route('/companies/<id>', methods=['GET'])
def get_company(id):
    company = mongo.db.companies.find_one({'_id': ObjectId(id)}, {'_id': 0})
    if company:
        return jsonify(company), 200
    else:
        return jsonify({'error': 'Company not found'}), 404

@app.route('/companies/<id>', methods=['PUT'])
def update_company(id):
    data = request.json
    mongo.db.companies.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'Company updated successfully'}), 200

@app.route('/companies/<id>', methods=['DELETE'])
def delete_company(id):
    mongo.db.companies.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Company deleted successfully'}), 200

# Employees CRUD

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    employee_id = mongo.db.employees.insert_one(data).inserted_id
    return jsonify({'message': 'Employee added successfully', 'id': str(employee_id)}), 201

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = list(mongo.db.employees.find({}, {'_id': 0}))
    return jsonify({'employees': employees}), 200

@app.route('/employees/<id>', methods=['GET'])
def get_employee(id):
    employee = mongo.db.employees.find_one({'_id': ObjectId(id)}, {'_id': 0})
    if employee:
        return jsonify(employee), 200
    else:
        return jsonify({'error': 'Employee not found'}), 404

@app.route('/employees/<id>', methods=['PUT'])
def update_employee(id):
    data = request.json
    mongo.db.employees.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'Employee updated successfully'}), 200

@app.route('/employees/<id>', methods=['DELETE'])
def delete_employee(id):
    mongo.db.employees.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Employee deleted successfully'}), 200

# Customers CRUD

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    customer_id = mongo.db.customers.insert_one(data).inserted_id
    return jsonify({'message': 'Customer added successfully', 'id': str(customer_id)}), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = list(mongo.db.customers.find({}, {'_id': 0}))
    return jsonify({'customers': customers}), 200

@app.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    customer = mongo.db.customers.find_one({'_id': ObjectId(id)}, {'_id': 0})
    if customer:
        return jsonify(customer), 200
    else:
        return jsonify({'error': 'Customer not found'}), 404

@app.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    mongo.db.customers.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'message': 'Customer updated successfully'}), 200

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    mongo.db.customers.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'Customer deleted successfully'}), 200


@app.route('/routes', methods=['GET'])
def describe_routes():
    routes = []
    for rule in app.url_map.iter_rules():
        route = {
            'methods': list(rule.methods),
            'endpoint': rule.endpoint,
            'path': str(rule)
        }
        routes.append(route)
    
    return jsonify({'routes': routes}), 200


if __name__ == '__main__':
    app.run(debug=True)