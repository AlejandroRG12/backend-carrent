import time
import bcrypt
from repositories.vehiculo_repository import VehiculoRepository
from models.vehiculo_model import Vehiculo

class VehiculoService:
    def __init__(self):
        self.repository = VehiculoRepository()

    def get_all_vehiculos(self):
        return self.repository.get_all_vehiculos()

    def get_vehiculo_by_id(self, id):
        return self.repository.get_vehiculo_by_id(id)

    def create_vehiculo(self, data_vehiculo):
        vehiculoNuevo = Vehiculo(**data_vehiculo)
        return self.repository.create_vehiculo(vehiculoNuevo.to_dict())

    def update_vehiculo(self, id_vehiculo, data_vehiculo):
        vehiculo = self.repository.get_vehiculo_by_id(id_vehiculo)
        if vehiculo:
            for key, value in data_vehiculo.items():
                setattr(vehiculo, key, value)
            return self.repository.update_vehiculo(id_vehiculo, vehiculo.to_dict())
        else:
            raise ValueError("Vehículo no encontrado")

    def delete_vehiculo(self, id_vehiculo):
        return self.repository.delete_vehiculo(id_vehiculo)