from flask import Flask, request
import uuid
import boto3
from flaskwebgui import FlaskUI

iam = boto3.resource('iam')
assume_role_policy = iam.AssumeRolePolicy('sssAdminEC2')

app = Flask(__name__)
ui = FlaskUI(app)


@app.route('/')
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <html>
    <head>
        <link rel="stylsheet" href="s3Upload.css">
    </head>
    <body>
        <div>
            <input type=file name=myfile>
            <input type=text name=rename placeholder="Rename File">
            <input type=submit>
            </form>
        <div>
    <body>
    </html>    
        '''


@app.route('/upload', methods=['POST'])


def upload():
    print(request.form)
    s3 = boto3.resource('s3')

    s3.Bucket('music-storage-cs493').put_object(
        Key='private/'+ request.form['rename'] +'.mp3', Body=request.files['myfile'])

    return '<h1>File saved to S3</h1>'



if __name__ == '__main__':
    ui.run()
