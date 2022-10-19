from flask import Flask
from flask_restx import Api, Resource

from src.server.instance import server
from src.server.getflightjson import getFlightJson

app, api = server.app, server.api

book_db = [
    {'id':0, 'title': 'War and Peace'},
    {'id':1, 'title': "Clean Code"}
]

flights_json = getFlightJson()


#Resource é o recurso reponsavel pelos verbos http
@api.route('/books')
class bookList(Resource):
    def get(self,):
        return flights_json