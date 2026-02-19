from faker import Faker
import pandas as pd
import sqlite3
import logging

logging.basicConfig(
    level = logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s '
)

fake = Faker()

def extract():
    data = []
    for i in range(10):
        data.append({
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "country": fake.country(),
            "email": fake.email(),
        })

    df = pd.DataFrame(data)
    df.to_csv('fake_data.csv', index=False)
    return df

def transform(df):
    df['fullname_name'] = df['first_name'] + '' + df['last_name']
    df.to_csv('transformed_data.csv', index=False)
    return df

if __name__ == "__main__":
    df = extract()
    logging.info("Donnees extraits et sauvegardees dans fake_data.csv")