from producer.generator import generate_csv_file
from app.insert_into_s3.insert_csv import insert_data_into_s3, s3_client
import time
import os
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(current_dir, '../../.env')

load_dotenv(dotenv_path)


if __name__ == '__main__':
    s3_bucket = "myetlprojectdata"
    local_data_folder = "/home/guiadurra/file_generator_etl/data"

    for i in range(4):
        generate_csv_file()
        time.sleep(5)
        insert_data_into_s3(local_data_folder=local_data_folder,s3_bucket=s3_bucket)
        

