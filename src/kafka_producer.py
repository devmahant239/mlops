import json
import logging
import time

from kafka import KafkaProducer
from data_generator import generate_transaction

logging.basicConfig(level=logging.INFO)


KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "transactions"
NUMBER_OF_MESSAGE = 5
MESSAGE_DELAY_SECONDS = 1


def create_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVER,
        value_serializer=lambda data: json.dumps(data).encode("utf-8")
    )
    return producer

def send_transactions():
    producer = create_kafka_producer()

    try:
        for i in range(NUMBER_OF_MESSAGE):
            transaction = generate_transaction()
            producer.send(KAFKA_TOPIC,value=transaction)
            logging.info(f"sent transaction to kafka:{transaction}")
            time.sleep(MESSAGE_DELAY_SECONDS)

        producer.flush()

        logging.info("All transaction sent succesfully")
    except Exception as error:
        logging.error(f"Failed to send transaction to kafka: {error}")

    finally:
        producer.close()
        logging.info("kafka producer closed")

if __name__ == "__main__":
    send_transactions()