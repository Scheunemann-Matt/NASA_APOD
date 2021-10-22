# __init__.py
from flask import Flask
import os
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")