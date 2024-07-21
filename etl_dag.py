from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from etl_pipeline import extract, transform, load
from data_quality import run_data_quality_checks, generate_data_quality_report

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'sales_etl_pipeline',
    default_args=default_args,
    description='ETL pipeline for sales data',
    schedule_interval=timedelta(days=1),
)

extract_task = PythonOperator(
    task_id='extract_data',
    python_callable=extract,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load_data',
    python_callable=load,
    dag=dag,
)

data_quality_task = PythonOperator(
    task_id='run_data_quality_checks',
    python_callable=run_data_quality_checks,
    op_kwargs={'expectations_path': 'expectations/sales_data_suite.json'},
    dag=dag,
)

report_task = PythonOperator(
    task_id='generate_data_quality_report',
    python_callable=generate_data_quality_report,
    op_kwargs={'output_path': '/reports/data_quality_report.txt'},
    dag=dag,
)

extract_task >> transform_task >> load_task >> data_quality_task >> report_task