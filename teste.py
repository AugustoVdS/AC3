import os 
from flask import Flask, jsonify, request
from math import sqrt
 
app = Flask(__name__)
@app.route('/')

def aaaa():
    primos = "<h1><b>tudo vai dar certo, prof!!</b></h1>"
    return primos 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
        
