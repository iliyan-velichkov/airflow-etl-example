def transform(**kwargs):
    # Retrieve extracted data
    extracted_data = kwargs['ti'].xcom_pull(key='extracted_data', task_ids='extract_task')

    # Transform data: Convert names to uppercase
    transformed_data = [
        (row[0], row[1].upper(), row[2].upper()) for row in extracted_data
    ]

    # Pass the transformed data to the next task
    kwargs['ti'].xcom_push(key='transformed_data', value=transformed_data)
