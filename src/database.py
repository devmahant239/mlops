import psycopg2

def get_connection():
    connection = psycopg2.connect(
        host ="localhost",
        port = 5434,
        database = "fraud_db",
        user = "admin",
        password = "admin123"
    )
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions(
        transaction_id VARCHAR(100),
        amount FLOAT,
        location VARCHAR(50),
        transaction_type VARCHAR(50),
        transaction_time TIMESTAMP,
        is_fraud BOOLEAN
    )
    """)

    connection.commit()
    cursor.close()
    connection.close()
    print("table created successfull")

def insert_transaction(transaction):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute("""
    INSERT INTO transactions(
        transaction_id,
        amount,
        location,
        transaction_type,
        transaction_time,
        is_fraud
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        transaction["transaction_id"],
        transaction["amount"],
        transaction["location"],
        transaction["transaction_type"],
        transaction["transaction_time"],
        transaction["is_fraud"]
    ))

    connection.commit()
    cursor.close()
    connection.close()

    print("Transaction inserted successfully")

if __name__ == "__main__":
    create_table()

