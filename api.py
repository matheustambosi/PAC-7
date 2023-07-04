from flask import Flask, request, jsonify
from flask_cors import CORS
import data_scraping

app = Flask(__name__)
CORS(app)

@app.route('/preview', methods=['POST'])
def sum_values():
    data = request.get_json()
    value1 = data['rooms']
    value2 = data['meters']

    result = data_scraping.preview(value1, value2)

    response = jsonify({'result': result[0]})

    return response

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    response = jsonify({'status': 'healthy'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()