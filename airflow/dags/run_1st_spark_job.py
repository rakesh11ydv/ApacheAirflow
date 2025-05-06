from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

dag = DAG(
    'spark_submit_dag',
    default_args=default_args,
    description='A simple Spark submit DAG',
    schedule_interval=None,  # Trigger manually
    start_date=datetime(2025, 5, 6),
    catchup=False,
)

spark_submit_command = """
spark-submit --class dataframe_op.ProductSalesAnalysis --master local[*] /opt/spark/app/SparkWithScalaLearn2024-assembly-0.1.0-SNAPSHOT.jar
"""

run_spark_job = DockerOperator(
    task_id='run_spark_job',
    image='spark-image',  # The image you built or pulled
    command=spark_submit_command,
    dag=dag,
    auto_remove=True,
    network_mode='host'
)

run_spark_job
