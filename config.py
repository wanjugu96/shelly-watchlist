import os

class Config:
    '''
    General configuration parent class
    '''
    '''
    contains configurations that are used in both production and development stages.
    '''
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    '''
    configurations that are used in production stages of our application
    '''
class ProdConfig(Config):
    pass

    
class  Devconfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True

config_options = {
'development':Devconfig,
'production':ProdConfig
}



