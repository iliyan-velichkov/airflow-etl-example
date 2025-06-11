import psycopg2

def extract(**kwargs):
    db_config = kwargs['db_config']
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Extract data
    cursor.execute("SELECT id, first_name, last_name FROM source_employees")
    rows = cursor.fetchall()

    # Pass the extracted data to the next task
    kwargs['ti'].xcom_push(key='extracted_data', value=rows)

    cursor.close()
    conn.close()
