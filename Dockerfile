FROM apache/airflow:2.1.4

WORKDIR /usr/src/
COPY ./dags/ .
COPY ./requirements.txt .

RUN airflow db init
RUN airflow users  \
        --username admin \
        --password admin \
        --firstname John \
        --lastname Doe \
        --role Admin \
        --email admin@example.com

CMD ["scheduler"]