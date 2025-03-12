FROM apache/airflow:2.5.1

# Atualizar os pacotes e instalar dependências necessárias antes do Java
USER root
RUN apt-get update && apt-get install -y curl gnupg && apt-get clean

# Instalar OpenJDK 11 (necessário para PySpark)
RUN apt-get update && apt-get install -y openjdk-11-jdk && apt-get clean

# Definir variável de ambiente do Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Voltar para o usuário airflow
USER airflow

# Instalar PySpark
RUN pip install pyspark
RUN pip install --no-cache-dir apache-airflow-providers-apache-spark