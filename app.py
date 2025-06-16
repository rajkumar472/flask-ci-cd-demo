# Triggering deploy from EC2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "return "Updated version deployed from GitHub!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
