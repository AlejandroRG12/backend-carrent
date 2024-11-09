from flask import jsonify, request, make_response   
from services.pago_service import PagoService
from helpers.response import ResponsePetition

class PagoController:
    
    def __init__(self):
        self.service = PagoService()

    def get_all_pagos(self):
        try:
            pagos = self.service.get_all_pagos()
            pagos_dict = [pago.to_dict() for pago in pagos]
            response = ResponsePetition('success', 200,'Pagos encontrados', pagos_dict)
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500,  str(e))
            return make_response(response.return_response(), 500)

    def get_pago_by_id(self, id):
        try:
            pago = self.service.get_pago_by_id(id)
            if pago:
                pago_dict = pago.to_dict()
                response = ResponsePetition('success', 200, 'Pago encontrado', pago_dict)
            else:
                response = ResponsePetition('error', 400, 'Pago no encontrado')
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500, str(e))
            return make_response(response.return_response(), 500)

    def create_pago(self):
        data = request.get_json()
        try:
            pago_id = self.service.create_pago(data)
            if 'error' in pago_id:
                response = ResponsePetition('error', 400, pago_id['error'])
                return make_response(response.return_response(), 400)
            response = ResponsePetition('success', 201,'Pago creado', {'id': pago_id})
            return make_response(response.return_response(), 201)
        except ValueError as e:
            response = ResponsePetition('error', 400, str(e))
            return make_response(response.return_response(), 400)
        
    def update_pago(self, id):
        data = request.get_json()
        try:
            pago_id = self.service.update_pago(id, data)
            if pago_id:
                response = ResponsePetition('success', 200, 'Pago actualizado', {'id': pago_id})
            else:
                response = ResponsePetition('error', 400, 'Pago no encontrado')
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500, str(e))
            return make_response(response.return_response(), 500)
        
    def delete_pago(self, id):
        try:
            pago_id = self.service.delete_pago(id)
            if pago_id:
                response = ResponsePetition('success', 200, 'Pago eliminado', {'id': pago_id})
            else:
                response = ResponsePetition('error', 400, 'Pago no encontrado')
            return make_response(response.return_response(), 200)
        except Exception as e:
            response = ResponsePetition('error', 500, str(e))
            return make_response(response.return_response(), 500)
            