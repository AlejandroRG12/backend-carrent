from flask import Blueprint
from controller.usuario_controller import UsuarioController

routes = Blueprint('routes', __name__)

"""
    - - - - - -  RUTAS DE USUARIOS  - - - - - -
"""
@routes.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    return UsuarioController().get_all_usuarios()

@routes.route('/usuarios/<string:id>', methods=['GET'])
def get_usuario_by_id(id):
    return UsuarioController().get_usuario_by_id(id)

@routes.route('/usuarios', methods=['POST'])
def create_usuario():
    return UsuarioController().create_usuario()