from flask import Flask
#from werkzeug.datastructures import T
# from .config import Devconfig
from flask_bootstrap import Bootstrap
from  config import config_options

bootstrap=Bootstrap()
def create_app(config_name):
    app=Flask(__name__)
    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extentions
    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    
    #will add the views and form
    return app



#Initializing application
#app=Flask(__name__,instance_relative_config=True)

#setting up configuration
#app.config.from_object(Devconfig)
#pp.config.from_pyfile('config.py')

#initializing Flask Extensions
# bootstrap=Bootstrap(app)

# from app import views
# from app import error