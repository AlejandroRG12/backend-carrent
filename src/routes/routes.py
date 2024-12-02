from flask import Blueprint
from controller.usuario_controller import UsuarioController
from controller.vehiculo_controller import VehiculoController
from controller.review_controller import ReviewController
from controller.renta_controller import RentaController
from controller.pago_controller import PagoController
from controller.auth_controller import AuthController

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

@routes.route('/usuarios/<string:id>', methods=['PUT'])
def update_usuario(id):
    return UsuarioController().update_usuario(id)

@routes.route('/usuarios/<string:id>', methods=['DELETE'])
def delete_usuario(id):
    return UsuarioController().delete_usuario(id)

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

"""
    - - - - - -  RUTAS DE REVIEWS  - - - - - -
"""
@routes.route('/reviews', methods=['GET'])
def get_all_reviews():
    return ReviewController().get_all_reviews()

@routes.route('/reviews/<string:id>', methods=['GET'])
def get_review_by_id(id):
    return ReviewController().get_review_by_id(id)

@routes.route('/reviews', methods=['POST'])
def create_review():
    return ReviewController().create_review()

@routes.route('/reviews/<string:id>', methods=['PUT'])
def update_review(id):
    return ReviewController().update_review(id)

@routes.route('/reviews/<string:id>', methods=['DELETE'])
def delete_review(id):
    return ReviewController().delete_review(id)

"""
    - - - - - -  RUTAS DE RENTAS  - - - - - -
"""
@routes.route('/rentas', methods=['GET'])
def get_all_rentas():
    return RentaController().get_all_rentas()

@routes.route('/rentas/<string:id>', methods=['GET'])
def get_renta_by_id(id):
    return RentaController().get_renta_by_id(id)

@routes.route('/rentas', methods=['POST'])
def create_renta():
    return RentaController().create_renta()

@routes.route('/rentas/<string:id>', methods=['PUT'])
def update_renta(id):
    return RentaController().update_renta(id)

@routes.route('/rentas/<string:id>', methods=['DELETE'])
def delete_renta(id):
    return RentaController().delete_renta(id)

"""
    - - - - - -  RUTAS DE PAGOS  - - - - - -
"""
@routes.route('/pagos', methods=['GET'])
def get_all_pagos():
    return PagoController().get_all_pagos()

@routes.route('/pagos/<string:id>', methods=['GET'])
def get_pago_by_id(id):
    return PagoController().get_pago_by_id(id)

@routes.route('/pagos', methods=['POST'])
def create_pago():
    return PagoController().create_pago()

@routes.route('/pagos/<string:id>', methods=['PUT'])
def update_pago(id):
    return PagoController().update_pago(id)

@routes.route('/pagos/<string:id>', methods=['DELETE'])
def delete_pago(id):
    return PagoController().delete_pago(id)

"""
    - - - - - -  RUTAS DE AUTH  - - - - - -
"""
@routes.route('/auth', methods=['POST'])
def login():
    return AuthController().login()
