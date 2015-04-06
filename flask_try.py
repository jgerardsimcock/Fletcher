
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/') 
def hello_world():
    return 'Stay Stoked!'

@app.route('/test')
def get_request():
  return redirect(url_for('static', filename='flask.html'))



if __name__ == '__main__':
    app.debug=True
    app.run(host = '0.0.0.0')