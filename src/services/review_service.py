from repositories.review_repository import ReviewRepository
from models.review_model import Review

class ReviewService:
    def __init__(self):
        self.repository = ReviewRepository()

    def get_all_reviews(self):
        return self.repository.get_all_reviews()

    def get_review_by_id(self, id):
        return self.repository.get_review_by_id(id)

    def create_review(self, data_review):
        reviewNuevo = Review(**data_review)
        return self.repository.create_review(reviewNuevo.to_dict())

    def update_review(self, id_review, data_review):
        review_data = self.repository.get_review_by_id(id_review)
        if review_data is None:
            raise ValueError("Review not found")
        
        # Convertir el diccionario a una instancia de Review
        review = Review.from_dict(review_data)
        
        # Actualizar los atributos de la instancia de Review
        for key, value in data_review.items():
            setattr(review, key, value)
        
        # Convertir la instancia de Review a un diccionario antes de pasarla al repositorio
        return self.repository.update_review(id_review, review.to_dict())

    def delete_review(self, id_review):
        return self.repository.delete_review(id_review)