class BaseConfig(object):
    'Base configuracion'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost:3306/almacen"

class ProductionConfig(BaseConfig):
    'Produccion configuracion'
    DEBUG = False
class DevelopmentConfig(BaseConfig):
    'Desarrollo configuracion'
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'Desarrollo key'










    # ! configuraciones de los entornos, prueba, desarollo y qa (configuramos lo que queremos que se pueda hacer en cada servidor de manera invividual  y lo pasamos a el run.pyy (nuestra app)