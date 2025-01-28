from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from tasks.extract_task import extract
from tasks.transform_task import transform
from tasks.load_task import load

# Database configuration (hardcoded)
DB_CONFIG = {
    "host": "postgres",
    "database": "postgres",
    "user": "custom_user",
    "password": "custom_password",
    "port": 5432
}

default_args = {
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG(
    'etl_students_dag',
    default_args=default_args,
    description='A modular ETL pipeline for students',
    schedule_interval=None,
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract,
        provide_context=True,
        op_kwargs={'db_config': DB_CONFIG}
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform,
        provide_context=True
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load,
        provide_context=True,
        op_kwargs={'db_config': DB_CONFIG}
    )

    extract_task >> transform_task >> load_task
