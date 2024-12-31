import boto3
import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(current_dir, '../../.env')

load_dotenv(dotenv_path)

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")

s3_client = boto3.client(
                        's3',
                        aws_access_key_id=AWS_ACCESS_KEY,
                        aws_secret_access_key=AWS_SECRET_KEY,
                        region_name="us-east-1"
                        )

def insert_data_into_s3(local_data_folder, s3_bucket):
    folders = os.listdir(local_data_folder)
    for folder in folders:
        folder_name = os.path.join(local_data_folder, folder)
        
        if os.path.isdir(folder_name):
            s3_folder = folder

            files = os.listdir(folder_name)
            
            for file in files:
                local_file_path = os.path.join(folder_name,file)

                

                if file.endswith(".csv"):
                    try:
                        s3_client.upload_file(local_file_path,s3_bucket,f"{s3_folder}/{file}")

                        os.remove(local_file_path)
                        print(f"local file {local_file_path} deleted")

                    except Exception as e:
                        print(f'Error uploading local file {local_file_path}: {e}') 







