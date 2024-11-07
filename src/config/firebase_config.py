import os
import firebase_admin
from firebase_admin import credentials, firestore

# ========================================================================================
# | IMPORTANTE!!!!!!!
# | Coloca el archivo que te proporcina firestore en la carpeta src/config/<NOMBRE_DE_TU_ARCHIVO>.json
# | y cambia el nombre del archivo en la siguiente línea
# ========================================================================================

def initialize_firebase():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    cred_path = os.path.join(base_dir, 'credentials.json') # Cambia el nombre del archivo si es necesario
    
    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"No se encontraron las credenciales de firebase en la ruta: {cred_path}")
    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    return firestore.client()