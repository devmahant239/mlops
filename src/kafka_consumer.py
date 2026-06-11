import logging 
import json 

from kafka import KafkaConsumer

logging.basicConfig(level=logging.INFO)

KAFKA_BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "transactions"
CONSUMER_GROUP = "fraud-consumer-group"


def create_kafka_consumer():
    consumer = KafkaConsumer(
        KAFKA_TOPIC,
        bootstrap_servers = KAFKA_BOOTSTRAP_SERVER,
        group_id = CONSUMER_GROUP,
        value_deserializer = lambda data: json.loads(data.decode("utf-8")),
        auto_offset_reset = "earliest"
    )
    return consumer


def consumer_transaction():
    consumer= create_kafka_consumer()
    logging.info("kafka consumer started, waiting for message")


    try:
        for message in consumer:
            transaction = message.value
            logging.info(f"received transaction:{transaction}")

    except Exception as error:
        logging.error(f"failed while consuming message:{error}")

    finally:
        consumer.close()
        logging.info("kafka consumer closed")


if __name__ == "__main__":
    consumer_transaction()        