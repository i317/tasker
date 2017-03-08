from flask import Flask, jsonify, request
from flask import render_template

app = Flask(__name__)


@app.route('/interactive/')
def interactive():
	return render_template('interactive.html')

@app.route('/background_process')
def background_process():
	try:
		lang = request.args.get('proglang', 0, type=str)
		if str(lang).lower() == '':
			return jsonify(result='Please enter an response.')
		else:
			return jsonify(result='Thank you for your response.')
	except Exception as e:
		return str(e)

if __name__ == '__main__':
    app.run(debug=True)