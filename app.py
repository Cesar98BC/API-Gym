from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) ## To allow direct AJAX calls

@app.route('/datos', methods=['GET'])
def home():
    r = requests.get('https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Arsenal')

    return r.json()

if __name__ == '__main__':
   app.run(debug = True)