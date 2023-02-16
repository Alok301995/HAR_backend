from flask import Flask
import os
from flask_cors import CORS
from src.routes.eval import eval

# Create Flask app


app = Flask(__name__,instance_relative_config = True)
CORS(app)

app.register_blueprint(eval)


# def create_app(test_config = None):
#     app = Flask(__name__,instance_relative_config = True)
#     CORS(app)
    
#     # if test_config is None:
#     #     app.config.from_mapping(
#     #         SECRET_KEY = os.environ.get('SECRET_KEY')
#     #     )
#     # else:
#     #     app.config.from_mapping(test_config)
        
        
#     # Here we will register our blueprint Routes
#     app.register_blueprint(eval)
    
        
#     return app