FROM bitnami/python
WORKDIR /Python_CRUD/
COPY /requirements.txt .
COPY /source ./source/
ENV PYTHONPATH .
RUN pip install -r ./requirements.txt

#similarly as running a python file
#CMD ["python", "-u", "source/app_tests/test_crud.py"]

#unitest call
CMD ["python", "-u", "-m", "unittest"]

#unitest call with tests directory
#CMD ["python", "-u", "-m", "unittest", "discover", "-s", "source/app_tests/"]