from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Cloudbuild Demo with a Flask Application. Current time is '+ str(datetime.datetime.now()) +'!</h1>'


@app.route('/about/')
def about():
    return '<h3>This is a Flask web application.</h3>'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
