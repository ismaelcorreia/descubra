from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
DB_URL=os.getenv('DB_URL')