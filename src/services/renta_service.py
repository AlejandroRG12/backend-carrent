from repositories.renta_repository import RentaRepository
from models.renta_model import Renta

class RentaService:
    def __init__(self):
        self.repository = RentaRepository()

    def get_all_rentas(self):
        return self.repository.get_all_rentas()

    def get_renta_by_id(self, id):
        return self.repository.get_renta_by_id(id)

    def create_renta(self, data_renta):
        rentaNueva = Renta(**data_renta)
        return self.repository.create_renta(rentaNueva.to_dict())

    def update_renta(self, id_renta, data_renta):
        renta_data = self.repository.get_renta_by_id(id_renta)
        if renta_data is None:
            raise ValueError("Renta not found")
        
        renta = Renta.from_dict(renta_data)
        
        for key, value in data_renta.items():
            setattr(renta, key, value)
        
        return self.repository.update_renta(id_renta, renta.to_dict())

    def delete_renta(self, id_renta):
        return self.repository.delete_renta(id_renta)