import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from app import app
from werkzeug.utils import secure_filename
import time

from dotenv import load_dotenv

load_dotenv()

# files = UploadSet("files", TEXT + DOCUMENTS + DATA, default_dest=lambda app: 'uploads')
# Configuração para armazenar os arquivos em uma pasta chamada "uploads"

UPLOAD_FOLDER = os.environ.get('UPLOAD_PATH')


# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def createIfNotExistsUploaFolder(folder_name=''):
    folder_name = f'{UPLOAD_FOLDER}/{folder_name}'
    folder_name = folder_name.replace(" ", "").lower()
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    return folder_name


def upload_file(filesForm, folder_name='', filename=int(time.time()), property_name='files'):
    folder_name = createIfNotExistsUploaFolder(folder_name)
    if not filesForm:
        return []
    files = filesForm.getlist(property_name)

    uploaded_files = []
    for file in files:
        if file.filename != '':
            file_extension = os.path.splitext(file.filename)[-1]
            final_filename = f"{filename+file_extension}"
            final_filename = f"{secure_filename(final_filename)}"
            # filename = f"{secure_filename(file.filename)}"
            file_path = os.path.join(folder_name, final_filename)
            file.save(file_path)
            uploaded_files.append(file_path)

    return uploaded_files
