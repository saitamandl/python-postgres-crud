FROM bitnami/python
COPY /requirements.txt /Python_CRUD
COPY /source /Python_CRUD/source
ENV PYTHONPATH /Python_CRUD/source
RUN pip install -r /Python_CRUD/requirements.txt
CMD ["python", "-u", "/Python_CRUD/source/app_tests/test_crud.py"]