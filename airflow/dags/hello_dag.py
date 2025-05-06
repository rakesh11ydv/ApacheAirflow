from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import time


# Define a Python function to be run by the task
def print_hello():
    print(f"Hello! The current date and time is: {datetime.now()}")


def sleep_task():
    print(f"Sleeping for 10 seconds...")
    time.sleep(10)
    print(f"Awoke from sleep at {datetime.now()}")


# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    'simple_test_dag',
    default_args=default_args,
    description='A simple test DAG',
    schedule_interval='@daily',  # This will run once a day
    start_date=datetime(2025, 5, 5),
    catchup=False,
)

# Define the tasks
task_1 = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

task_2 = PythonOperator(
    task_id='sleep_task',
    python_callable=sleep_task,
    dag=dag,
)

# Set the task order
task_1 >> task_2
