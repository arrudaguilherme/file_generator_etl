from faker import Faker
from datetime import datetime
import random
import os
import pandas as pd
import time

fake = Faker("en_US")

def generate_sales_data():
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
        sale = {
            "transaction_id": fake.uuid4(),  
            "product_id": fake.uuid4(),  
            "product_name": fake.word().capitalize(),  
            "category": fake.random_element(["Electronics", "Clothing", "Books", "Home Appliances", "Toys"]),  
            "brand": fake.company(),  
            "quantity": random.randint(1, 20),  
            "price_per_unit": round(random.uniform(10, 1000), 2),  
            "discount_percentage": random.choice([0, 5, 10, 15, 20]),  
            "discount_value": None,  
            "total_value": None,  
            "sale_date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),  
            "payment_method": fake.random_element(["Credit Card", "Debit Card", "Cash", "Online Payment", "Gift Card"]),  
            "customer_type": fake.random_element(["New", "Returning", "VIP"]),  
            "store_location": fake.city(),  
            "region": fake.random_element(["North", "South", "East", "West", "Central"]),  
            "sales_representative": fake.name(),  
            "shipping_cost": round(random.uniform(5, 50), 2),  
            "delivery_time_days": random.randint(1, 7),  
            "customer_feedback": fake.random_element(["Positive", "Neutral", "Negative", "None"]),  
        }
        
        sale["discount_value"] = round(sale["price_per_unit"] * (sale["discount_percentage"] / 100), 2)
        sale["total_value"] = round(sale["quantity"] * (sale["price_per_unit"] - sale["discount_value"]) + sale["shipping_cost"], 2)
        
        return sale
    except Exception as e:
        print(f"Error generating sales data: {e}")

def generate_user_data():
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
    except Exception as e:
        print(f"Error generating sales data: {e}")

def generate_csv_file():
    temp_user_data_list = []
    temp_sales_data_list = []
    for i in range(10000):
        temp_user_list = [generate_user_data()]
        temp_sales_list = [generate_sales_data()]
        temp_user_df = pd.DataFrame(temp_user_list)
        temp_sales_df = pd.DataFrame(temp_sales_list)    
        temp_user_data_list.append(temp_user_df)
        temp_sales_data_list.append(temp_sales_df)
    user_df_final = pd.concat(temp_user_data_list)
    sales_df_final = pd.concat(temp_sales_data_list)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S_%f")
    path_sales = os.path.join("data/sales",f"sales_{date}.csv")
    path_users = os.path.join("data/users",f"users_{date}.csv")
    sales_df_final.to_csv(path_sales,sep=",",index=False,encoding="utf-8")
    user_df_final.to_csv(path_users,sep=",",index=False,encoding="utf-8")

    

if __name__ == '__main__':
        while True:
            generate_csv_file()
            time.sleep(0.2)
 

    