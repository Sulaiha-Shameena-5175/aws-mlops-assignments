from flask import Flask
import boto3

app = Flask(__name__)

@app.route("/")
def list_files():
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
    return "<p>pass</p>"
    