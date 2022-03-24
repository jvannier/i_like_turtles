from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


class Quotes(Resource):
    """First test class"""

    @app.route('/test/')
    def test():
        param = request.args.get('param')
        return json.dumps({'success':True, 'param': param}), 200, {'ContentType':'application/json'}

    def get(self):
        return {
            "Hello": "world",
            "query_parap": "{value}"
            }


if __name__ == '__main__':
    app.run(debug=True)
