from flask import Flask , render_template
import os
from flask_cors import CORS
from src.routes.eval import eval
from src.routes.home import home

# Create Flask app


app = Flask(__name__,instance_relative_config = True)
CORS(app)


app.register_blueprint(home)
app.register_blueprint(eval)
