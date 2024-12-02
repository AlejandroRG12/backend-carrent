from flask import jsonify, request, make_response   
from services.usuario_service import UsuarioService
from helpers.response import ResponsePetition

class UsuarioController:

    def __init__(self):
        self.service = UsuarioService()

    def get_all_usuarios(self):
        try:
            usuarios = self.service.get_all_usuarios()
            usuarios_dict = [usuario.to_dict() for usuario in usuarios]
            response = ResponsePetition('success', 200,'Usuarios encontrados', usuarios_dict)
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500,  str(e))
            return make_response(response.return_response(), 500)

    def get_usuario_by_id(self, id):
        try:
            usuario = self.service.get_usuario_by_id(id)
            if usuario:
                usuario_dict = usuario.to_dict()
                response = ResponsePetition('success', 200, 'Usuario encontrado', usuario_dict)
            else:
                response = ResponsePetition('error', 400, 'Usuario no encontrado')
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500, str(e))
            return make_response(response.return_response(), 500)

    def create_usuario(self):
        data = request.get_json()
        try:
            user_id = self.service.create_usuario(data)
            if 'error' in user_id:
                response = ResponsePetition('error', 400, user_id['error'])
                return make_response(response.return_response(), 400)
            response = ResponsePetition('success', 201,'Usuario creado', {'id': user_id})
            return make_response(response.return_response(), 201)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)
        
    def update_usuario(self, id):
        data = request.get_json()
        try:
            user_id = self.service.update_usuario(id, data)
            if 'error' in user_id:
                response = ResponsePetition('error', 400, user_id['error'])
                return make_response(response.return_response(), 400)
            response = ResponsePetition('success', 200, 'Usuario actualizado', {'id': user_id})
            return make_response(response.return_response(), 200)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)
        
    def delete_usuario(self, id):
        try:
            user_id = self.service.delete_usuario(id)
            if 'error' in user_id:
                response = ResponsePetition('error', 400, user_id['error'])
                return make_response(response.return_response(), 400)
            response = ResponsePetition('success', 200, 'Usuario eliminado', {'id': user_id})
            return make_response(response.return_response(), 200)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)