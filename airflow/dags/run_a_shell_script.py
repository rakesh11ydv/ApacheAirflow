from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'airflow',
    'retries': '1',
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    dag_id='bash_dag',
    description='run a bash script',
    default_args=default_args,
    schedule_interval=None,
    start_date=datetime(2025, 5, 6),
    catchup=False
)

run_bash_command = BashOperator(
    task_id='run_bash_command',
    dag=dag,
    bash_command='echo "Hello from Airflow at $(date)"'
)

run_bash_script = BashOperator(
    task_id='run_bash_script',
    dag=dag,
    bash_command='bash /opt/airflow/jars/hello.sh'
)

start = EmptyOperator(task_id='start')
end = EmptyOperator(task_id='end')

start >> run_bash_command >> run_bash_script >> end
