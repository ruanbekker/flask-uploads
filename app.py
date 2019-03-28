import os
from uuid import uuid4 as uuid
from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    ext = file.filename.split('.')[-1]
    filename = file.filename.encode('hex')[1:18] + '.' + ext
    f = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(f)

    return render_template('result.html', filename=filename)

@app.route('/uploads/<string:filename>', methods=['GET'])
def serve_img(filename):
    print(filename)
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run()
