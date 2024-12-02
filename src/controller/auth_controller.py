import asyncio
from flask import jsonify, request, make_response   
from services.auth_service import AuthService
from helpers.response import ResponsePetition

class AuthController:

    def __init__(self):
        self.service = AuthService()

    def login(self):
        data = request.get_json()
        try:
            user = self.service.login(data['usuario'], data['password'])
            if user is None:
                response = ResponsePetition('error', 400, 'Usuario o contraseña incorrectos')
                return make_response(response.return_response(), 400)
            response = ResponsePetition('success', 200, 'Usuario autenticado', user)
            return make_response(response.return_response(), 200)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)