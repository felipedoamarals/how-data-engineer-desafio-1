from db_utils import Database
from dotenv import load_dotenv
import os
import pandas as pd
import datetime
import json

load_dotenv("../.env")

class DataIngestion:
    def __init__(self, source_csv, source_json):
        self.db = Database(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            database_name=os.getenv("DB_NAME")    
        )
        self.source_csv = source_csv
        self.source_json = source_json

    def connect_db(self):
        self.db.connect()

    def disconnect_db(self):
        self.db.disconnect()

    def ingest_csv(self):
        for file in os.listdir(self.source_csv):
            file_dir = os.path.join(self.source_csv, file)

            table_name = ((os.path.splitext(file)[0]).split('(')[0]).replace(' ', "_").lower()

            df = pd.read_csv(file_dir, header=0, delimiter=',')

            df = df.drop(df.columns[0], axis=1)

            df.insert(0, "id", range(1, 1 + len(df)))

            now = datetime.datetime.now()
            df.insert(len(df.columns), "created_at", now)

            df.to_sql(name=table_name, con=self.db.engine, if_exists="replace", index=False, index_label="id")

    def ingest_json(self):
        for file in os.listdir(self.source_json):

            if not file.endswith('.json'):
                continue

            file_dir = os.path.join(self.source_json, file)

            table_name = "top-tech-startups-hiring-2023"

            with open(file_dir, "r") as f:
                data = json.load(f)
            
            df = pd.json_normalize(data)

            df = df.rename(columns={"id": "startups_id"})

            now = datetime.datetime.now()
            df.insert(len(df.columns), "created_at", now)

            df.to_sql(name=table_name, con=self.db.engine, if_exists="replace", index=False, index_label="startup_id")

if __name__ == "__main__":
    di = DataIngestion(
        source_csv="../datasets/nba-players-and-team-data/",
        source_json="../datasets/top-tech-startups-hiring-2023/"
    )

    di.connect_db()

    di.ingest_csv()
    di.ingest_json()

    di.disconnect_db()