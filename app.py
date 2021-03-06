from flask import Flask
import os
import socket
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World from %s' % socket.gethostname()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
