
class Config(object):
    """
    Common Config
    """

class DevelopmentConfig(Config):
    """
    Development Config
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
    }

