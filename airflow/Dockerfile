FROM openjdk:8-jre-slim

# Install Spark
RUN apt-get update && apt-get install -y wget \
    && wget -qO- https://archive.apache.org/dist/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz | tar xvz -C /opt \
    && mv /opt/spark-3.2.1-bin-hadoop3.2 /opt/spark

ENV SPARK_HOME=/opt/spark
ENV PATH=$SPARK_HOME/bin:$PATH

# Copy the jar file into the image (adjust the path to your local file)
COPY C:/Users/Rakesh_Yadav/IdeaProjects/ApacheAirflow/airflow/jars/SparkWithScalaLearn2024-assembly-0.1.0-SNAPSHOT.jar /opt/airflow/jars/SparkWithScalaLearn2024-assembly-0.1.0-SNAPSHOT.jar
