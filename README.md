# Apache Airflow Project

- create .env file
- use this docker file to spin up airflow using docker
- id and password is airflow
- dag UI - http://localhost:8080/
- create dags in /airflow/dags folder
- run `docker compose up airflow-init` and then `docker compose up`

# Dependency resolve
- install python which support airflow (3.9.x)
- install airflow using pip along with python constraints
    -  pip install "apache-airflow==2.8.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.9.txt"
