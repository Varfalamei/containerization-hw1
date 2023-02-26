from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'myself',
    'start_date': datetime(2023, 2, 26),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

with DAG(
    'my_dag',
    default_args=default_args,
    schedule_interval=timedelta(seconds=5),
) as dag:

    t1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello world"',
        dag=dag,
    )

    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
        dag=dag,
    )

    t2.set_upstream(t1)