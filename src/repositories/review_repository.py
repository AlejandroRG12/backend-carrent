from config.firebase_config import initialize_firebase
from models.review_model import Review

class ReviewRepository:
    def __init__(self):
        self.db = initialize_firebase()
        self.collection = self.db.collection('reviews')

    def get_all_reviews(self):
        reviews = []
        for doc in self.collection.stream():
            review_data = doc.to_dict()
            review_data['id'] = doc.id  # Añadir el ID del documento al diccionario
            reviews.append(Review.from_dict(review_data))
        return reviews

    def get_review_by_id(self, id):
        doc = self.collection.document(id).get()
        return doc.to_dict() if doc.exists else None

    def create_review(self, data_review):
        doc = self.collection.document()
        doc.set(data_review)  # Aquí eliminamos la llamada a to_dict
        return doc.id

    def update_review(self, review_id, data_review):
        doc = self.collection.document(review_id)
        doc.update(data_review)
        return doc.id

    def delete_review(self, review_id):
        self.collection.document(review_id).delete()
        return review_id