import os



class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DB_URI = os.environ.get('PG_URL')


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DB_URI = os.environ.get('PG_TEST_URL') 


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DB_URI = os.environ.get('PG_URL') 