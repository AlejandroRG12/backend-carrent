from flask import jsonify, request, make_response   
from services.renta_service import RentaService
from helpers.response import ResponsePetition

class RentaController:
            
    def __init__(self):
        self.service = RentaService()

    def get_all_rentas(self):
        try:
            rentas = self.service.get_all_rentas()
            rentas_dict = [renta.to_dict() for renta in rentas]
            response = ResponsePetition('success', 200,'Rentas encontrados', rentas_dict)
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500,  str(e))
            return make_response(response.return_response(), 500)

    def get_renta_by_id(self, id):
        try:
            renta = self.service.get_renta_by_id(id)
            if renta:
                renta_dict = renta.to_dict()
                response = ResponsePetition('success', 200, 'Renta encontrado', renta_dict)
            else:
                response = ResponsePetition('error', 400, 'Renta no encontrado')
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500, str(e))
            return make_response(response.return_response(), 500)

    def create_renta(self):
        data = request.get_json()
        try:
            renta_id = self.service.create_renta(data)
            response = ResponsePetition('success', 201, 'Renta creado', {'id': renta_id})
            return make_response(response.return_response(), 201)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)

    def update_renta(self, id):
        data = request.get_json()
        try:
            renta_id = self.service.update_renta(id, data)
            response = ResponsePetition('success', 'Renta actualizado', {'id': renta_id})
            return make_response(response.return_response(), 200)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)
        
    def delete_renta(self, id):
        try:
            renta_id = self.service.delete_renta(id)
            if 'error' in renta_id:
                response = ResponsePetition('error', 400, renta_id['error'])
                return make_response(response.return_response(), 400)
            response = ResponsePetition('success', 200,'Renta eliminado', {'id': renta_id})
            return make_response(response.return_response(), 200)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)
        