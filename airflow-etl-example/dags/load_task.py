import psycopg2

def load(**kwargs):
    db_config = kwargs['db_config']
    # Retrieve transformed data
    transformed_data = kwargs['ti'].xcom_pull(key='transformed_data', task_ids='transform_task')

    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    for row in transformed_data:
        cursor.execute("""
            INSERT INTO TARGET_STUDENTS (ID, FIRST_NAME, LAST_NAME)
            VALUES (%s, %s, %s)
            ON CONFLICT (ID) DO UPDATE
            SET FIRST_NAME = EXCLUDED.FIRST_NAME,
                LAST_NAME = EXCLUDED.LAST_NAME
        """, row)

    conn.commit()
    cursor.close()
    conn.close()
