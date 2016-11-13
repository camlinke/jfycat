from app import app
from flask import render_template
import requests
import json
import random

@app.route('/')
def home():
    url = "https://api.gfycat.com/v1test/gfycats/search?search_text=jeff&count=50"
    r = requests.get(url)
    jeffs = json.loads(r.text)['gfycats']
    src = random.choice(jeffs)['gfyName']
    return render_template('home.html', src=src)