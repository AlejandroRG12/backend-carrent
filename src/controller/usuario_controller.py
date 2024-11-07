from flask import jsonify, request
from services.usuario_service import UsuarioService
from helpers.response import ResponsePetition

class UsuarioController:

    def __init__(self):
        self.service = UsuarioService()

    def get_all_usuarios(self):
        try:
            usuarios = self.service.get_all_usuarios()
            usuarios_dict = [usuario.to_dict() for usuario in usuarios]
            response = ResponsePetition('success', 'Usuarios encontrados', usuarios_dict)
            return response.return_response()
        except Exception as e:
            response = ResponsePetition('error', str(e))
            return response.return_response()

    def get_usuario_by_id(self, id):
        usuario = self.service.get_usuario_by_id(id)
        return jsonify(usuario) if usuario else jsonify({'Empleado no encontrado': True})

    def create_usuario(self):
        data = request.get_json()
        try:
            user_id = self.service.create_usuario(data)
            return jsonify({'id': user_id}), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400