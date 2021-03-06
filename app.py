import threading
from flask import Flask,jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import os
import sys

data = None
app = Flask(__name__)
cors = CORS(app)
api = Api(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def init_webhooks(base_url):
    # Update inbound traffic via APIs to use the public-facing ngrok URL
    pass

def create_app():
    
    # Initialize our ngrok settings into Flask
    app.config.from_mapping(
        BASE_URL="http://localhost:5000",
        USE_NGROK=os.environ.get("USE_NGROK", "False") == "True" and os.environ.get("WERKZEUG_RUN_MAIN") != "true"
    )

    if app.config.get("ENV") == "development" and app.config["USE_NGROK"]:
        # pyngrok will only be installed, and should only ever be initialized, in a dev environment
        from pyngrok import ngrok

        # Get the dev server port (defaults to 5000 for Flask, can be overridden with `--port`
        # when starting the server
        port = sys.argv[sys.argv.index("--port") + 1] if "--port" in sys.argv else 5000

        # Open a ngrok tunnel to the dev server
        public_url = ngrok.connect(port).public_url
        print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

        # Update any base URLs or webhooks to use the public ngrok URL
        app.config["BASE_URL"] = public_url
        init_webhooks(public_url)

    # ... Initialize Blueprints and the rest of our app

    return app

class Settings(Resource):
    @cross_origin()
    def post(self, param):
          return {
        'status' : 'done',
        'value' : param
        }

class Data(Resource):
    @cross_origin()
    def get(self):
        return jsonify(data)

class Stats(Resource):
    @cross_origin()
    def get(self):
        return {
            'success_rate':0.90
        }
class Root(Resource):
    @cross_origin()
    def get(self):
          return "= Hawkeye ="
     

api.add_resource(Data, "/data")
api.add_resource(Root, "/")
api.add_resource(Settings, "/settings/<string:param>")
api.add_resource(Stats, "/stats")

def start():
    threading.Thread(target=app.run).start()
    