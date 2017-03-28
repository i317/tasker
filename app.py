from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/interactive/')
def interactive():
	return render_template('interactive.html')

@app.route('/interactive/', methods=['POST'])
def result_post():
    response = request.form['proglang']
    return response

if __name__ == '__main__':
    app.run(debug=True)