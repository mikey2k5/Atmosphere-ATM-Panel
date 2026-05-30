import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'atm_secret_key_super_secret_1337_futuristic')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///atm.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secure session configs
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
