from flask import jsonify

from flask .ext.restful import Resource

import models

class CourseList(Resource):
    def get(self):
        return jsonify({'reviews': [{'course': 1, 'rating': 5}]})

class CourseList(Resource):
    def get(self, id):
        return jsonify({'course': 1, 'rating': 5})

    def put(self, id):
            return jsonify({'course': 1, 'rating': 5})

    def delete(self, id):
        return jsonify({'course': 1, 'rating': 5})
