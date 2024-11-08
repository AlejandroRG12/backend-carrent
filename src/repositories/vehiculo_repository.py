from config.firebase_config import initialize_firebase
from models.vehiculo_model import Vehiculo

class VehiculoRepository:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection('vehiculos')

    def get_all_vehiculos(self):
        docs = self.collection.stream()
        vehiculos = []
        for doc in docs:
            vehiculo_data = doc.to_dict()
            vehiculo_data['id'] = doc.id
            vehiculos.append(Vehiculo.from_dict(vehiculo_data))
        return vehiculos

    def get_vehiculo_by_id(self, vehiculo_id):
        doc = self.collection.document(vehiculo_id).get()
        if doc.exists:
            vehiculo_data = doc.to_dict()
            vehiculo_data['id'] = doc.id
            return Vehiculo.from_dict(vehiculo_data)
        else:
            return None

    def create_vehiculo(self, data_vehiculo):
        doc = self.collection.document()
        doc.set(data_vehiculo)
        return doc.id

    def update_vehiculo(self, id_vehiculo, data_vehiculo):
        doc_ref = self.collection.document(id_vehiculo)
        doc_ref.update(data_vehiculo)
        return id_vehiculo

    def delete_vehiculo(self, id_vehiculo):
        self.collection.document(id_vehiculo).delete()
        return id_vehiculo