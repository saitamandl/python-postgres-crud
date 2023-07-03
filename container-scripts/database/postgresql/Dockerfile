FROM bitnami/postgresql
COPY /.utils/certificates/ssl.db.cert.pem /bitnami/postgresql/certificates/
COPY /.utils/certificates/ssl.db.key /bitnami/postgresql/certificates/
COPY /container-scripts/database/postgresql/data/py_pg_crud.sql /docker-entrypoint-initdb.d/py_pg_crud.sql
#RUN ssl=on
#RUN ssl_cert_file=/bitnami/postgresql/ssl.db.cert.pem
#RUN ssl_cert_file=/bitnami/postgresql/ssl.db.key.pem
