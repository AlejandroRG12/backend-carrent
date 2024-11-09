from flask import jsonify, request, make_response   
from services.review_service import ReviewService
from helpers.response import ResponsePetition

class ReviewController:
        
        def __init__(self):
            self.service = ReviewService()
    
        def get_all_reviews(self):
            try:
                reviews = self.service.get_all_reviews()
                reviews_dict = [review.to_dict() for review in reviews]
                response = ResponsePetition('success', 200,'Reviews encontrados', reviews_dict)
                return make_response(response.return_response(), 200)
            except Exception as e:
                response = ResponsePetition('error', 500,  str(e))
                return make_response(response.return_response(), 500)
    
        def get_review_by_id(self, id):
            try:
                review = self.service.get_review_by_id(id)
                if review:
                    review_dict = review.to_dict()
                    response = ResponsePetition('success', 200, 'Review encontrado', review_dict)
                else:
                    response = ResponsePetition('error', 400, 'Review no encontrado')
                return make_response(response.return_response(), 200)
            except Exception as e:
                response = ResponsePetition('error', 500, str(e))
                return make_response(response.return_response(), 500)
    
        def create_review(self):
            data = request.get_json()
            try:
                review_id = self.service.create_review(data)
                response = ResponsePetition('success', 201, 'Review creado', {'id': review_id})
                return make_response(response.return_response(), 201)
            except ValueError as e:
                response = ResponsePetition('error', 400, str(e))
                return make_response(response.return_response(), 400)
    
        def update_review(self, id):
            data = request.get_json()
            try:
                review_id = self.service.update_review(id, data)
                response = ResponsePetition('success', 'Review actualizado', {'id': review_id})
                return make_response(response.return_response(), 200)
            except ValueError as e:
                response = ResponsePetition('error', 400, str(e))
                return make_response(response.return_response(), 400)
            
        def delete_review(self, id):
            try:
                review_id = self.service.delete_review(id)
                if 'error' in review_id:
                    response = ResponsePetition('error', 400, review_id['error'])
                    return make_response(response.return_response(), 400)
                response = ResponsePetition('success', 200,'Review eliminado', {'id': review_id})
                return make_response(response.return_response(), 200)
            except ValueError as e:
                response = ResponsePetition('error', 400, str(e))
                return make_response(response.return_response(), 400)