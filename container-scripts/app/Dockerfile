FROM bitnami/python
COPY /.utils/certificates/ssl.db.cert.pem /Python_CRUD/certificates/
COPY /.utils/certificates/ssl.db.key /Python_CRUD/certificates/
COPY /requirements.txt /Python_CRUD
COPY /app /Python_CRUD/app
ENV PYTHONPATH /Python_CRUD
RUN pip install -r /Python_CRUD/requirements.txt
CMD ["python", "-u", "/Python_CRUD/app/main.py"]