import bcrypt
from flask import jsonify
from config.firebase_config import initialize_firebase
from helpers.response import ResponsePetition

class AuthRepository:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection('usuarios')

    def login(self, usuario):
        query = self.collection.where('usuario', '==', usuario).get()
        # Combinar datos del documento con su ID
        result = [{**doc.to_dict(), 'id': doc.id} for doc in query]
        return result[0] if result else None

