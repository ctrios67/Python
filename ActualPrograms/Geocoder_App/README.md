## Synopsis

This is an application where the user can upload a CSV file that contains a column named "Address" or "address"
and the application will geocode the addresses in that column, append the Latitude & Longitude as new columns in the
CSV file, display the new CSV in the webpage, and allow the user to download the new file.

Application View to User: 
![alt text](https://github.com/ctrios67/Python/blob/master/ActualPrograms/Geocoder_App/sample.png "Visual Example")

## Code Example

Python code for website server via flask
```@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploaded', methods=['POST'])
def uploaded():
    global upload
    if(request.method=='POST'):
        upload = request.files['file']
        extension = upload.filename[-4:]
        if(extension == '.csv'):
            newfilename = secure_filename('uploaded' + upload.filename)
            upload.save(newfilename)
            handleUpload.readfile(newfilename)
            if(handleUpload.containsAddress()==True):
                handleUpload.addingLatLon()
                handleUpload.newCSV()
                return render_template('index.html', btn='download.html', content=handleUpload.render())
            else:
                return render_template('index.html', text='The file you uploaded does\
                not have a column named "Address" or "address" Please choose a file\
                 that abides by that so.')
        else:
            return render_template('index.html', text='The file you uploaded\
            is not a CSV file. Please reupload with a CSV file.')

@app.route('/download')
def download():
    return send_file(secure_filename('uploaded'+upload.filename), attachment_filename='yourfile.csv',
     as_attachment=True)

if __name__ == '__main__':
    app.run()
```

Code for handling the uploaded CSV file

```
class geoCSV:
    def readfile(self,uploadedfile):
        global df
        df = pandas.read_csv(uploadedfile)
        #df = pandas.read_csv('table.csv')

    # If this fails, tell flask "this ain't following the rules"
    def containsAddress(self):
        try:
            df['Address']
            return True
        except KeyError:
            print('No Address column in the file.')
            return False

    def containsaddress(self):
        try:
            df['address']
            return True
        except KeyError:
            print('No address column was found.')
            return False

    def addingLatLon(self):
        global df
        latitude = []
        longitude = []
        geolocator = Nominatim()
        for index, row in df.iterrows():
            location = geolocator.geocode(row['Address'])
            latitude.append(location.latitude)
            longitude.append(location.longitude)
        df['Latitude'] = latitude
        df['Longitude'] = longitude
        #print(df)

    def newCSV(self):
        global df
        df.to_csv('yourfile.csv')

    def render(self):
        df = pandas.read_csv('yourfile.csv')
        return df.to_html()

handleUpload = geoCSV()
```

## Motivation

The end of a Udemy course I am taking challenges the student to complete this task with as minimal as resources as
possible. This app combines almost everything I have learned in that course and since I went into this course knowing
jack squat about Python, I figured I'd see if I can make this!

## Installation

Just clone this git repo after installing the dependencies pandas, flask, & geopy via
```
pip3 install pandas
pip3 install flask
pip3 install geopy
```
