from flask import jsonify, request
from main.main import app
from main.servec import MainServec


@app.route('/', methods=['GET'])
def api():
    data = {
        'message': 'Hello, World!'
    }
    return jsonify(data)


@app.route('/marketChatbot/api/v1/randomProduct', methods=['GET'])
def random_products():
    products = MainServec.get_three_random_products()
    return jsonify(products)


@app.route('/marketChatbot/api/v1', methods=['POST'])
def get_product_by_code():
    code = request.args.get('code')
    product = MainServec.get_product_by_code(code)
    return jsonify(product)
