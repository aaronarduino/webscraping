import os

# General Flask app settings
DEBUG = os.environ.get('DEBUG', None)
SECRET_KEY = os.environ.get('SECRET_KEY', None)
