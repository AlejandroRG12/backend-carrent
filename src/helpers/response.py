from flask import jsonify

class ResponsePetition:
    def __init__(self, status='', message='', data=[]):
        self.status = status
        self.message = message
        self.data = data

    def __str__(self):
        return f"{self.status}: {self.message} - {self.data}"
    
    def return_response(self):
        return jsonify({
            'status': self.status,
            'message': self.message,
            'data': self.data
        })
