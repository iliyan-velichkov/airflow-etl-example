import psycopg2

def load(**kwargs):
    db_config = kwargs['db_config']
    # Retrieve transformed data
    transformed_data = kwargs['ti'].xcom_pull(key='transformed_data', task_ids='transform_task')

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    for row in transformed_data:
        cursor.execute("""
            INSERT INTO target_employees (id, first_name, last_name)
            VALUES (%s, %s, %s)
            ON CONFLICT (id) DO UPDATE
            SET first_name = EXCLUDED.first_name,
                last_name = EXCLUDED.last_name
        """, row)

    conn.commit()
    cursor.close()
    conn.close()
