import os


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    SECRET_KEY = 'very_secret'


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('PG_URL')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('PG_TEST_URL') 


class ProductionConfig(BaseConfig):
    url = os.environ.get("PG_URL")

    if url is not None and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = url