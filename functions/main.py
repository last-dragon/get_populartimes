# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`

from firebase_functions import https_fn
from firebase_admin import initialize_app

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_cors import cross_origin
import populartimes
from dotenv import dotenv_values

app = Flask(__name__)
cors = CORS(app)

env_vars = dotenv_values("./.env")
api_key = env_vars["REACT_APP_GOOGLE_MAPS_API_KEY"]

@app.route('/api/getpopulartime', methods=['POST'])
@cross_origin()
def my_function():
    # Retrieve data from the request
    data = request.get_json()

    # Call your Python function with the provided data
    result = get_popular_time(data)

    # Return the result as a JSON response
    return jsonify(result)

def get_popular_time(data):
    place_id = data.get("placeId")
    result = populartimes.get_id(api_key, place_id)
    return {'message': 'Popular Times', 'data': result}

if __name__ == '__main__':
    app.run()

# initialize_app()
#
#
# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")