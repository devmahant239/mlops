import random
import uuid 
import json
import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO)

NUMBER_OF_TRANSACTIONS = 5

OUTPUT_FILE = "data/raw/transactions_json"

location = ["ahmedabad", "mumbai", "banglore", "delhi"]

transaction_type = ["atm","online", "pos", "bank_transfer"]


def generate_transaction():
    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "amount": random.randint(100,100000),
        "location":random.choice(location),
        "transaction_type":random.choice(transaction_type),
        "transaction_time":datetime.now().isoformat(),
        "is_fraud": random.choice([True, False])
    }

    return transaction

if __name__ == "__main__":

    transactions = []

    for i in range(NUMBER_OF_TRANSACTIONS):

        try:

            new_transaction = generate_transaction()

            transactions.append(new_transaction)

            transaction_json = json.dumps(new_transaction)

            logging.info(f"Generated transection: {transaction_json}")

        except Exception as error:

            logging.error(f"Generated transection failed:{error}")

    with open(OUTPUT_FILE, "w") as file:

        json.dump(transactions, file, indent=4)


    logging.info(
        f"Transactions saved successfully: {OUTPUT_FILE}"
    )