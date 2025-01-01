from producer.generator import generate_csv_file
from app.insert_into_s3.insert_csv import insert_data_into_s3
from app.database.db import Base, create_engine, DB_URL
from app.load_into_db.load import process_and_insert_files
import time
import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

current_dir = os.path.dirname(os.path.abspath(__file__))

dotenv_path = os.path.join(current_dir, '../../.env')

load_dotenv(dotenv_path)

engine = create_engine(DB_URL)



if __name__ == '__main__':
    s3_bucket = "myetlprojectdata"
    local_data_folder = os.getenv("local_data_folder")

    folders = ["feedback", "marketing_campaigns", "product_categories", "products", "sales", "shipping", "users"]


    generate_csv_file()
    time.sleep(10)
    insert_data_into_s3(local_data_folder=local_data_folder,s3_bucket=s3_bucket)
    time.sleep(10)
    process_and_insert_files("myetlprojectdata",folders)
    time.sleep(10)
    

