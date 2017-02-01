from flask import jsonify, Blueprint

from flask .ext.restful import Resource

import models

class CourseList(Resource):
    def get(self):
        return jsonify({'courses': [{'title': 'Python Basics'}]})

class CourseList(Resource):
    def get(self, id):
        return jsonify({'title': 'Python Basics'})

    def put(self, id):
            return jsonify({'title': 'Python Basics'})

    def delete(self, id):
        return jsonify({'title': 'Python Basics'})

courses_api = Blueprint('resources.courses', __name__)
