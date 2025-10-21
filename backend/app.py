import os
import requests
import json
from dotenv import load_dotenv
import flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RL_API_HOST = os.getenv("RL_API_HOST")

@app.route('/stats', methods=['GET'])

def getPlayerStats():
    playerName = request.args.get('playerName')
    platform = request.args.get('platform', 'epic')

    if not playerName:
        return jsonify({"error": "Missing 'playerName' parameter"}), 400
    