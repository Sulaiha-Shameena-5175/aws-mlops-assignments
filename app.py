from flask import Flask
import boto3

app = Flask(__name__)

@app.route("/folders")
def list_files():

    prefix = 'home/sulaiha.shameena/'

    session = boto3.Session(profile_name='pe-mle-user-role')
    s3 = session.client('s3')

    list_obj = s3.list_objects_v2(Bucket = 'tiger-mle-pg', Prefix = prefix, Delimiter='/')
    folders_response = list_obj.get('CommonPrefixes', [])
    folder_dict = dict()

    for folder in folders_response: 
        main_folder = folder['Prefix'].replace(prefix,'')
        file_list = s3.list_objects_v2(Bucket = 'tiger-mle-pg', Prefix = folder['Prefix'])
        files = (file_list.get('Contents', []))
        folder_dict[main_folder] = []

        for eachFile in files: 
            if (eachFile['Key'].endswith('.txt')):
                sub_folder = eachFile['Key'].replace(folder['Prefix'], '')
                folder_dict[main_folder].append(sub_folder)
                
    return folder_dict
    