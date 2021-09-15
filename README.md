# Airflow Training Repo

Repo for my Airflow Training

## Clone to Local

```bash
git clone https://github.com/bobquest33/airflow_training_09_21.git
```

## Pull latest changes


```bash
git pull origin master
```

## Env Setup

```
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
```

## How to Run


Stop Containers

```bash
docker-compose down
```

Build Airflow Config (Only required when doing clean build)

```bash
docker-compose build --pull --no-cache
```

Run airflow-init to setup airflow database (To be run first time)

```bash
docker-compose up airflow-init
```

Running airflow - Up

```bash
docker-compose -f docker-compose.yml up -d --remove-orphans
```

Access the Airflow UI
http://127.0.0.1:8080/

u:airflow
p:airflow
