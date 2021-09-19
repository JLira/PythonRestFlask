from flask import Flask
from flask_restful import Api
from resources.Hotel import Hoteis, Hotel

app = Flask(__name__)
api = Api(app)

hoteis = [{
    'hotel_id': 'alpha', 
    'nome': 'Alpha Hotel',
    'estrelas': 4.3,
    'diaria':420.30, 
    'cidade': 'Rio de Janeiro'
},
{
    'hotel_id': 'bravo', 
    'nome': 'Bravo Hotel',
    'estrelas': 3.5,
    'diaria':320.80, 
    'cidade': 'Sta Catarina'
}, 
{
    'hotel_id': 'charlie', 
    'nome': 'Charlie Hotel',
    'estrelas': 5,
    'diaria':790.00, 
    'cidade': 'Sao Paulo'
}
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')



if __name__ == '__main__':
    app.run(debug=True)
