from faker import Faker
from datetime import datetime
import random
import os
import pandas as pd
import time

fake = Faker("en_US")

def ensure_directory_exists(path):
    absolute_path = os.path.abspath(path)
    if not os.path.exists(absolute_path):
        os.makedirs(absolute_path)

def generate_sales_data(user_ids):
    try:
        sale = {
            "transaction_id": fake.uuid4(),
            "user_id": random.choice(user_ids),
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
            "user_id": fake.uuid4(),  
            "name": fake.name(),
            "birth_date": fake.date_of_birth().isoformat(),
            "gender": fake.random_element(["M", "F"]),
            "phone_number": fake.phone_number(),
            "email": fake.email(),
            "address": fake.address(),
            "postal_code": fake.postcode(),
            "city": fake.city(),
            "state": fake.state(),
            "country": fake.country(),
            "profession": fake.job(),
            "company": fake.company(),
            "language": fake.language_name(),
            "marrital_status": fake.boolean(),
            "date_generated": datetime.now().strftime("%Y-%m-%d %H:%M:%S_%f")
        }
        return user
    except Exception as e:
        print(f"Error generating user data: {e}")

def generate_shipping_data(transaction_ids):
    try:
        shipping = {
            "shipping_id": fake.uuid4(),
            "transaction_id": random.choice(transaction_ids), 
            "shipping_date": fake.date_time_this_month().strftime("%Y-%m-%d %H:%M:%S"),
            "delivery_date": fake.future_date(end_date='+30d').strftime("%Y-%m-%d"),
            "shipping_cost": round(random.uniform(5, 50), 2),
            "carrier": fake.company(),
            "status": fake.random_element(["In Transit", "Delivered", "Cancelled"]),
        }
        return shipping
    except Exception as e:
        print(f"Error generating shipping data: {e}")

def generate_marketing_campaign_data(user_ids):
    try:
        campaign = {
            "campaign_id": fake.uuid4(),
            "user_id": random.choice(user_ids),
            "campaign_name": fake.bs().title(),
            "channel": fake.random_element(["Email", "SMS", "Social Media", "Direct Mail"]),
            "start_date": fake.date_this_year().strftime("%Y-%m-%d"),
            "end_date": fake.future_date(end_date='+60d').strftime("%Y-%m-%d"),
            "budget": round(random.uniform(500, 5000), 2),
            "status": fake.random_element(["Active", "Completed", "Cancelled"]),
        }
        return campaign
    except Exception as e:
        print(f"Error generating marketing campaign data: {e}")

def generate_customer_feedback_data(user_ids, transaction_ids):
    try:
        feedback = {
            "feedback_id": fake.uuid4(),
            "user_id": random.choice(user_ids),  # Relacionado com `users`
            "transaction_id": random.choice(transaction_ids),  # Relacionado com `sales`
            "feedback_date": fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S"),
            "rating": random.randint(1, 5),
            "comments": fake.text(max_nb_chars=200),
        }
        return feedback
    except Exception as e:
        print(f"Error generating customer feedback data: {e}")

def generate_product_category_data():
    try:
        category = {
            "category_id": fake.uuid4(),
            "category_name": fake.random_element(["Electronics", "Clothing", "Books", "Home Appliances", "Toys"]),
            "description": fake.text(max_nb_chars=200),
        }
        return category
    except Exception as e:
        print(f"Error generating product category data: {e}")

def generate_product_data(category_ids):
    try:
        product = {
            "product_id": fake.uuid4(),
            "category_id": random.choice(category_ids),
            "product_name": fake.word().capitalize(),
            "brand": fake.company(),
            "price_per_unit": round(random.uniform(10, 1000), 2),
        }
        return product
    except Exception as e:
        print(f"Error generating product data: {e}")


def generate_csv_file():
    temp_user_data_list = []
    temp_sales_data_list = []
    temp_shipping_data_list = []
    temp_campaign_data_list = []
    temp_feedback_data_list = []
    temp_category_data_list = []
    temp_product_data_list = []


    # users data
    for _ in range(1000):
        temp_user_list = [generate_user_data()]
        temp_user_df = pd.DataFrame(temp_user_list)
        temp_user_data_list.append(temp_user_df)

    user_df_final = pd.concat(temp_user_data_list)
    user_ids = user_df_final["user_id"].tolist()

    # sales data
    for _ in range(5000):
        temp_sales_list = [generate_sales_data(user_ids)]
        temp_sales_df = pd.DataFrame(temp_sales_list)
        temp_sales_data_list.append(temp_sales_df)

    sales_df_final = pd.concat(temp_sales_data_list)
    transaction_ids = sales_df_final["transaction_id"].tolist()

    # shipping
    for _ in range(2000):
        temp_shipping_list = [generate_shipping_data(transaction_ids)]
        temp_shipping_df = pd.DataFrame(temp_shipping_list)
        temp_shipping_data_list.append(temp_shipping_df)

    # marketing data
    for _ in range(100):
        temp_campaign_list = [generate_marketing_campaign_data(user_ids)]
        temp_campaign_df = pd.DataFrame(temp_campaign_list)
        temp_campaign_data_list.append(temp_campaign_df)

    # feedback data
    for _ in range(2000):
        temp_feedback_list = [generate_customer_feedback_data(user_ids, transaction_ids)]
        temp_feedback_df = pd.DataFrame(temp_feedback_list)
        temp_feedback_data_list.append(temp_feedback_df)

    # product category data
    for _ in range(10):
        temp_category_list = [generate_product_category_data()]
        temp_category_df = pd.DataFrame(temp_category_list)
        temp_category_data_list.append(temp_category_df)

    category_df_final = pd.concat(temp_category_data_list)
    category_ids = category_df_final["category_id"].tolist()

    # product data
    for _ in range(200):
        temp_product_list = [generate_product_data(category_ids)]
        temp_product_df = pd.DataFrame(temp_product_list)
        temp_product_data_list.append(temp_product_df)

    product_df_final = pd.concat(temp_product_data_list)

    ensure_directory_exists("data/users")
    ensure_directory_exists("data/sales")
    ensure_directory_exists("data/shipping")
    ensure_directory_exists("data/marketing_campaigns")
    ensure_directory_exists("data/feedback")
    ensure_directory_exists("data/product_categories")
    ensure_directory_exists("data/products")

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S_%f")
    user_df_final.to_csv(f"data/users/users_{date}.csv", index=False, encoding="utf-8")
    sales_df_final.to_csv(f"data/sales/sales_{date}.csv", index=False, encoding="utf-8")
    pd.concat(temp_shipping_data_list).to_csv(f"data/shipping/shipping_{date}.csv", index=False, encoding="utf-8")
    pd.concat(temp_campaign_data_list).to_csv(f"data/marketing_campaigns/campaigns_{date}.csv", index=False, encoding="utf-8")
    pd.concat(temp_feedback_data_list).to_csv(f"data/feedback/feedback_{date}.csv", index=False, encoding="utf-8")
    category_df_final.to_csv(f"data/product_categories/categories_{date}.csv", index=False, encoding="utf-8")
    product_df_final.to_csv(f"data/products/products_{date}.csv", index=False, encoding="utf-8")


 

    