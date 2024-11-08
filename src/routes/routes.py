from flask import Blueprint
from controller.usuario_controller import UsuarioController
from controller.vehiculo_controller import VehiculoController

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

"""
    - - - - - -  RUTAS DE VEHICULOS  - - - - - -
"""
@routes.route('/vehiculos', methods=['GET'])
def get_all_vehiculos():
    return VehiculoController().get_all_vehiculos()

@routes.route('/vehiculos/<string:id>', methods=['GET'])
def get_vehiculo_by_id(id):
    return VehiculoController().get_vehiculo_by_id(id)

@routes.route('/vehiculos', methods=['POST'])
def create_vehiculo():
    return VehiculoController().create_vehiculo()

@routes.route('/vehiculos/<string:id>', methods=['PUT'])
def update_vehiculo(id):
    return VehiculoController().update_vehiculo(id)

@routes.route('/vehiculos/<string:id>', methods=['DELETE'])
def delete_vehiculo(id):
    return VehiculoController().delete_vehiculo(id)