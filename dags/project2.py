from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime


with DAG(
    dag_id="project2",
    default_args={"owner": "airflow"},
    start_date=days_ago(1),
    schedule_interval='@monthly',
    catchup=False,
) as dag:

    # criar tabela com os dados do arquivo csv
    import_csv = PostgresOperator(
        task_id='import_csv',
        postgres_conn_id='postgres_conn',
        sql="""
        COPY staging_hr FROM '/tmp/hr_data1.csv'
        DELIMITER ',' CSV HEADER;
        """
    )

    # separar os dados em tabelas
    insert_employees = PostgresOperator(
        task_id='insert_employees',
        postgres_conn_id='postgres_conn',
        sql='CALL update_employees();'
    )

    insert_jobs = PostgresOperator(
        task_id='insert_jobs',
        postgres_conn_id='postgres_conn',
        sql='CALL update_jobs();'
    )

    insert_department = PostgresOperator(
        task_id='insert_department',
        postgres_conn_id='postgres_conn',
        sql='CALL update_department();'
    )

    insert_employee_department = PostgresOperator(
        task_id='insert_employee_department',
        postgres_conn_id='postgres_conn',
        sql='CALL update_employee_departments()'
    )

    insert_salaries = PostgresOperator(
        task_id='insert_salaries',
        postgres_conn_id='postgres_conn',
        sql='CALL update_salaries();'
    )

    clear_staging = PostgresOperator(
        task_id='clear_staging',
        postgres_conn_id='postgres_conn',
        sql="CALL truncate_table('staging_hr');"
    )

import_csv >> insert_department >> insert_employees >> insert_jobs >> insert_employee_department >> insert_salaries >> clear_staging