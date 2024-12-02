from flask import jsonify, request, make_response   
from services.vehiculo_service import VehiculoService
from helpers.response import ResponsePetition

class VehiculoController:
    
        def __init__(self):
            self.service = VehiculoService()
    
        def get_all_vehiculos(self):
            try:
                vehiculos = self.service.get_all_vehiculos()
                vehiculos_dict = [vehiculo.to_dict() for vehiculo in vehiculos]
                response = ResponsePetition('success', 200,'Vehiculos encontrados', vehiculos_dict)
                return make_response(response.return_response(), 200)
            except Exception as e:
                response = ResponsePetition('error', 500,  str(e))
                return make_response(response.return_response(), 500)
    
        def get_vehiculo_by_id(self, id):
            try:
                vehiculo = self.service.get_vehiculo_by_id(id)
                if vehiculo:
                    vehiculo_dict = vehiculo.to_dict()
                    response = ResponsePetition('success', 200, 'Vehiculo encontrado', vehiculo_dict)
                else:
                    response = ResponsePetition('error', 400, 'Vehiculo no encontrado')
                return make_response(response.return_response(), 200)
            except Exception as e:
                response = ResponsePetition('error', 500, str(e))
                return make_response(response.return_response(), 500)
    
        def create_vehiculo(self):
            data = request.get_json()
            try:
                vehiculo_id = self.service.create_vehiculo(data)
                response = ResponsePetition('success', 201, 'Vehiculo creado', {'id': vehiculo_id})
                return make_response(response.return_response(), 201)
            except ValueError as e:
                response = ResponsePetition('error', 400, str(e))
                return make_response(response.return_response(), 400)
    
        def update_vehiculo(self, id):
            data = request.get_json()
            try:
                vehiculo_id = self.service.update_vehiculo(id, data)
                response = ResponsePetition('success', 200, 'Vehículo actualizado', {'id': vehiculo_id})
                return make_response(response.return_response(), 200)
            except ValueError as e:
                response = ResponsePetition('error', 400, str(e))
                return make_response(response.return_response(), 400)
            
        def delete_vehiculo(self, id):
            try:
                vehiculo_id = self.service.delete_vehiculo(id)
                if 'error' in vehiculo_id:
                    response = ResponsePetition('error', 400, vehiculo_id['error'])
                    return make_response(response.return_response(), 400)
                response = ResponsePetition('success', 200,'Vehiculo eliminado', {'id': vehiculo_id})
                return make_response(response.return_response(), 200)
            except ValueError as e:
                response = ResponsePetition('error', 400, str(e))
                return make_response(response.return_response(), 400)