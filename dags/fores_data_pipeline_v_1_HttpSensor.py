from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.sensors.http_sensor import HttpSensor

default_args = { 
    "owner" : "airflow",
    "start_date" : days_ago(2),
    "depends_on_past" : False,
    "email_on_failure" : False,
    "email_on_retry" : False,
    "email" : "youremail@host.com",
    "retries" : 1,
    "retry_delay" : timedelta(minutes=5)
 }

with DAG(dag_id="Forex_data_pipeline_http_sensor_v_1", 
          schedule_interval="@daily", 
          default_args=default_args, 
          catchup=False) as dag:
     is_forex_rates_available = HttpSensor(
         task_id = "is_forex_rates_available",
         method = 'GET',
         http_conn_id ='forex_api',
         endpoint='latest',
         response_check=lambda response: "rates" in response.text,
         poke_interval = 5,
         timeout=20
     )
