from flask import Blueprint
from flask import current_app

blueprint = Blueprint('hello', __name__, url_prefix='/hello')

@blueprint.route("/say", methods=["GET"])
def say_hello():
    return "Hello {}!".format(current_app.config.get('MY_ENV_VAR'))