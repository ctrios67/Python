## Synopsis

This is an application where the user can upload a CSV file that contains a column named "Address" or "address"
and the application will geocode the addresses in that column, append the Latitude & Longitude as new columns in the
CSV file, display the new CSV in the webpage, and allow the user to download the new file.

Application View to User:
![alt text](https://github.com/ctrios67/Python/tree/master/Geocoder_App/sample.png "Visual Example")

## Code Example

Python code for website server via flask
```
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
```

Code for handling the uploaded CSV file

```
class geoCSV:
    def readfile(self,uploadedfile):
        global df
        df = pandas.read_csv(uploadedfile, index_col=0)
        #df = pandas.read_csv('sample.csv')

    # If this fails, tell flask "this ain't following the rules"
    def containsAddress(self):
        # lowerUpper is 0 if Address is a column, 1 if its address
        global lowerUpper
        # Both existing comes first in order to notify the user immediately
        # otherwise it would erroneously process the file
        if( (('address') in df.columns) and (('Address') in df.columns) ):
            return False
        elif ('Address') in df.columns:
            lowerUpper = 0
            return True
        elif ('address') in df.columns:
            lowerUpper = 1
            return True
        else:
            #print('No address column was found.')
            return False

    def addingLatLon(self):
        global df
        global lowerUpper
        latitude = []
        longitude = []
        geolocator = Nominatim()
        if(lowerUpper==0):
            for index, row in df.iterrows():
                location = geolocator.geocode(row['Address'])
                latitude.append(location.latitude)
                longitude.append(location.longitude)
        else:
            for index, row in df.iterrows():
                location = geolocator.geocode(row['address'])
                latitude.append(location.latitude)
                longitude.append(location.longitude)
        df['Latitude'] = latitude
        df['Longitude'] = longitude
        #print(df)

    # This generates the new file with the new columns, but this may actually
    # not even be necessary.
    def newCSV(self):
        global df
        df.to_csv('yourfile.csv')

    # This is the least painful way to generate our new CSV file additions
    # Within the browser. This converts it into an HTML table.
    def render(self):
        global df
        # I am embarassed by the amount of time it took me to figure out how to
        # pass a CSS class to the genrated HTML table....
        return df.to_html(classes='download')

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
