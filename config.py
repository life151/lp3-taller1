"""
Configuración de la aplicación Flask
"""

# Configuración para el entorno de desarrollo
class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuración para el entorno de producción
class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'  # En producción se recomienda usar PostgreSQL o MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Configuración para pruebas
class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Diccionario para seleccionar la configuración según el entorno
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
