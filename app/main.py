from flask import Flask, jsonify
from service import get_current_btc_price

app = Flask(__name__)

@app.route('/bitcoin-price', methods=['GET'])
def hello():
    return jsonify(get_current_btc_price())

if __name__ == '__main__':
    app.run(debug=True)