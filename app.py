# This example uses the Evervault Python SDK.
import evervault
from flask import Flask, request, render_template, jsonify
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

@app.route("/")
def index():
    '''
    A function that returns the index page and passes in the Ev credentials.
    '''
    app_id=os.environ.get("APP_ID")
    team_id=os.environ.get("TEAM_ID")
    url=os.environ.get("URL")
    return render_template('index.html', app_id=app_id, team_id=team_id, url=url)
if __name__ == '__main__':
   app.run()

@app.route("/decrypt", methods=['POST'])
def decrypt():
    '''
    A function that calls the Evervault Function and returns the decrypted data.
    '''
    # Initialize the client with your app's API key
    evervault.init(os.environ.get("API_KEY"))

    decrypted_obj = evervault.run("decrypt-python", request.json)
    decrypted_name = decrypted_obj['result']['decryptedData']['name']
    
    return jsonify({'name': decrypted_name})