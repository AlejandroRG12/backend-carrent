from config.firebase_config import initialize_firebase
from models.renta_model import Renta

class RentaRepository:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection('rentas')

    def get_all_rentas(self):
        rentas = []
        for doc in self.collection.stream():
            renta_data = doc.to_dict()
            renta_data['id'] = doc.id
            rentas.append(Renta.from_dict(renta_data))
        return rentas

    def get_renta_by_id(self, id):
        doc = self.collection.document(id).get()
        if doc.exists:
            return Renta.from_dict(doc.to_dict())
        else:
            return None

    def create_renta(self, data_renta):
        doc = self.collection.document()
        doc.set(data_renta)  # Asegurarse de que data_renta sea un diccionario
        return doc.id

    def update_renta(self, renta_id, data_renta):
        doc = self.collection.document(renta_id)
        doc.update(data_renta)
        return doc.id

    def delete_renta(self, renta_id):
        self.collection.document(renta_id).delete()
        return renta_id