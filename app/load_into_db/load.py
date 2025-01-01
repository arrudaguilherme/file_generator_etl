import boto3
import os
import sys
from dotenv import load_dotenv
from app.database.db import create_engine, DB_URL, sessionmaker
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

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

def list_files_s3(bucket_name, folder_name):
    """Listar arquivos em uma pasta no S3."""
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)
    file_keys = []
    if 'Contents' in response:
        for obj in response['Contents']:
            if obj['Key'].endswith('.csv'):
                file_keys.append(obj['Key'])
    return file_keys

def read_data(bucket, key):
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    df = pd.read_csv(obj['Body'])
    return df

def insert_data_into_db(df, table_name):
    engine = create_engine(DB_URL)  # Certifique-se de que o DB_URL está configurado corretamente
    Session = sessionmaker(bind=engine)
    session = Session()  # Criar uma sessão

    try:
        # Usar pandas para inserir dados na tabela
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        session.commit()  # Commit após inserção bem-sucedida
        print(f"Data inserted into {table_name}")
    except Exception as e:
        session.rollback()  # Se houver erro, reverter transação
        print(f"Error occurred: {e}")
    finally:
        session.close()
        

def process_and_insert_files(bucket, folders):
    for folder in folders:
        print(f"Processing folder: {folder}")
        files = list_files_s3(bucket, folder)
        df_final = pd.DataFrame()
        for file_key in files:
            print(f"Reading file: {file_key}")
            df = read_data(bucket, file_key)
            print(f"appending {file_key} into df")
            df_final = pd.concat([df_final,df],ignore_index=True)
        insert_data_into_db(df_final, folder)
        print(f"Finished processing folder: {folder}")
            

