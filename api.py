from flask import Flask, request, jsonify
import data_scraping

app = Flask(__name__)

@app.route('/preview', methods=['POST'])
def sum_values():
    data = request.get_json()
    value1 = data['value1']
    value2 = data['value2']
    data_scraping.preview(value1, value2)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run()