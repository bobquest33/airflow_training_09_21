FROM apache/airflow:2.2.0b1-python3.9
COPY requirements.txt .
RUN pip install -r requirements.txt