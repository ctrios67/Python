#! /usr/bin/env python3
# backend.py - Backend of Geocoder App that is built via flask.
from flask import Flask, render_template, request, send_file, Response
from werkzeug import secure_filename
from latlon import handleUpload

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploaded', methods=['POST'])
def uploaded():
    global upload
    if(request.method=='POST'):
        upload = request.files['file']
        extension = upload.filename[-4:]
        # Check if it's a CSV file, otherwise tell the user.
        if(extension == '.csv'):
            newfilename = secure_filename('uploaded' + upload.filename)
            upload.save(newfilename)
            handleUpload.readfile(newfilename)
            # Check if file contains an Address column, otherwise tell user.
            if(handleUpload.containsAddress()==True):
                handleUpload.addingLatLon()
                handleUpload.newCSV()
                return render_template('index.html', btn='download.html', content=handleUpload.render())
            else:
                return render_template('index.html', text='The file you uploaded either does\
                not have a column named "Address", "address", or possibly contains both. \
                Please upload a file containing only 1 "address" or "Address" column.')
        else:
            return render_template('index.html', text='The file you uploaded\
            is not a CSV file. Please reupload with a CSV file.')

@app.route('/download')
def download():
    return send_file('yourfile.csv',
    attachment_filename='yourfile.csv',
     as_attachment=True)

if __name__ == '__main__':
    #app.debug=True
    app.run()
