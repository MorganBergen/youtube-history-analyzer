from flask import Flask, render_template, request, redirect, url_for, jsonify

import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        data = json.load(file)
        # process the data here
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

