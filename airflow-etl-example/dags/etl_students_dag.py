import sys
import os

# add the *parent* directory of the DAG file to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# now explicitly add the `tasks/` directory to sys.path too
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasks'))

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from tasks.extract_task import extract
from tasks.transform_task import transform
from tasks.load_task import load

# database configuration (hardcoded)
DB_CONFIG = {
    "host": "postgres",
    "database": "postgres",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}

default_args = {
    'start_date': datetime(2025, 1, 1),
    'retries': 1
}

with DAG(
    dag_id='etl_students_dag',
    default_args=default_args,
    description='A modular ETL pipeline for students',
    schedule=None,  # Explicit name (Airflow 3 prefers it)
    catchup=False,
    tags=['etl']
) as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract,
        op_kwargs={'db_config': DB_CONFIG}
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load,
        op_kwargs={'db_config': DB_CONFIG}
    )

    extract_task >> transform_task >> load_task
