import os
from dotenv import load_dotenv
import requests
from flask import Flask, request
from flask_cors import CORS

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", default="")
DEBUG = bool(os.environ.get("DEBUG", default=True))

if not UNSPLASH_KEY:
    raise EnvironmentError(
        "Please create .env.local file and insert the UNSPLASH_KEY in that file"
    )

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG


@app.route("/new-image")
def new_image():
    word = request.args.get("query")  # type: ignore the line
    headers = {"Accept-Version": "v1", "Authorization": "Client-ID " + UNSPLASH_KEY}
    params = {"query": word}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)

    data = response.json()
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
