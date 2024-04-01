import os
from pathlib import Path


class Config:
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY')

    PROJECT_NAME = 'video_bookmark_app'

    BASE_DIR = Path(__file__).parent.parent.parent
    DB_PATH = os.path.join(BASE_DIR, "sqlite.db")
    
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"

