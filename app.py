from flask import Flask,render_template,request
import os
app=Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check if the upload folder exists, if not, create it
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template("csv.html")

@app.route('/csv',methods=["GET","POST"])
def csv():
    if 'files[]' not in request.files:
        return 'No file part'
    files = request.files.getlist('files[]')
    for file in files:
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("back.html")

if __name__=='__main__':
    app.run()