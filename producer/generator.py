from faker import Faker
from datetime import datetime
import os
import pandas as pd
import time

fake = Faker("en_US")

def generate_data():
    try:
        user = {
            "name": fake.name(),
            "birth_date":fake.date_of_birth().isoformat(),
            "gender":fake.random_element(["M","F"]),
            "phone_number":fake.phone_number(),
            "email":fake.email(),
            "address":fake.address(),
            "postal_code":fake.postcode(),
            "city":fake.city(),
            "state":fake.state(),
            "country":fake.country(),
            "profession":fake.job(),
            "company":fake.company(),
            "language":fake.language_name(),
            "marrital_status":fake.boolean(),
            "date_generated":datetime.now().strftime("%Y-%m-%d %H:%M:%S_%f")
        }
        return user
    except:
        print("Error generating user data!")

def generate_csv_file(range_files:int):
    user_data_list = []
    for i in range(range_files):
        user_data = [generate_data()]
        df = pd.DataFrame(user_data)
        user_data_list.append(df)
    df_final = pd.concat(user_data_list)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S_%f")
    path = os.path.join("data",f"user{date}.csv")
    df_final.to_csv(path,sep=",",index=False,encoding="utf-8")

    

if __name__ == '__main__':
    while True:
        generate_csv_file(1000)
        time.sleep(0.5)
    # for i in range(10):
    #     result = generate_data()
    #     for item in result.items():
    #         print(item)
 

    