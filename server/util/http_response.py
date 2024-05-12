from datetime import datetime
from flask import jsonify

def httpResponseBody(data, message, status_code):
    return jsonify({
        'data': data,
        'message': message,
        'status_code': status_code,
        'datetime': datetime.now().isoformat()  # Convert datetime to ISO format
    })

def httpResponseBodyJson(data, message, status_code):
    return jsonify({
        'data': data,
        'message': message,
        'status_code': status_code,
        'datetime': datetime.now().isoformat()  # Convert datetime to ISO format
    })