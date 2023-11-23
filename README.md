# python CRUD operation

Containerized (docker) database (PostgreSQL) and python app for a simple CRUD (Create, Read, Update and Delete)
operation.

[//]: # (Database &#40;postgresql&#41; docker container and python app container is used to run a simple CRUD &#40;Create, Read, Update and Delete&#41; operation.)

## Docker Container

### Dockerfile

> [!NOTE]
> Source (host) path is dependent on the `context` path in [docker-compose.yml](docker-compose.yml) e.g. [line](
> docker-compose.yml](docker-compose.yml#L5).

#### Database (PostgreSQL)

A [Dockerfile](container-scripts/database/postgresql/Dockerfile) for the database is created.

1. `bitnami/postgresql` image is used
    - [Line 1](container-scripts/database/postgresql/Dockerfile#L1) -> `FROM bitnami/postgresql`
1. `COPY` command is used to copy the file [py_pg_crud.sql](container-scripts/database/postgresql/data/py_pg_crud.sql)
   to `/docker-entrypoint-initdb.d/` from host to docker.
   [py_pg_crud.sql](container-scripts/database/postgresql/data/py_pg_crud.sql) initialize the PostgreSQL database.
    - [Line 2](container-scripts/database/postgresql/Dockerfile#L2) -> `COPY /container-scripts/database/postgresql/data/py_pg_crud.sql /docker-entrypoint-initdb.d/py_pg_crud.sql`

#### App (python)

A [Dockerfile](container-scripts/app/Dockerfile) for the app is created.

1. `bitnami/python` image is used
    - [Line 1](container-scripts/app/Dockerfile#L1) -> `FROM bitnami/python`
1. `COPY` command is used to Copy the `requirements.txt` and source code to a directory in docker e.g. `Python_CRUD`.
    - [Line 2](container-scripts/app/Dockerfile#L2) -> `COPY /requirements.txt /Python_CRUD/`.
    - [Line 3](container-scripts/app/Dockerfile#L3) -> `COPY /source /Python_CRUD/source`.
1. Set environment variable `PYTHONPATH` to provide guidance to the Python interpreter about where to find various
   libraries and applications.
    - [Line 4](container-scripts/app/Dockerfile#L4) -> `ENV PYTHONPATH /Python_CRUD/source`.
1. Use the `requirements.txt` to install required dependencies to run or test the project.
    - [Line 5](container-scripts/app/Dockerfile#L5) -> `RUN pip install -r /Python_CRUD/requirements.txt`.

1. Run the unit-tests to test the app.
    - [Line 6](container-scripts/app/Dockerfile#L6) -> `CMD ["python", "-u", "/Python_CRUD/source/app_tests/test_crud.py"]`.

### dpcker-compose

[docker-compose.yml](docker-compose.yml) uses the [Dockerfiles](#dockerfile) to build images then spin up
the [database](docker-compose.yml#L3) and [app](docker-compose.yml#L21) services.

1. In the [services](docker-compose.yml#L2) specification name of the services are defined.
   This project used [database](docker-compose.yml#L3) and [app](docker-compose.yml#L21).
1. The individual service specifies the abstract definition of the computing resources.
1. Each service needs a build specification either in the form of `Dockerfile` or the `image` url.
1. `context` defines path/url to a directory containing a Dockerfile.
   Alternatively, it can also be used as the build `context`, this project uses project directory as the build
   context to resolve relative paths. e.g. [Line 5](docker-compose.yml#L5) -> `context: ./`
1. `dockerfile` sets an alternate Dockerfile. The relative path is resolved from the build `context`.
   e.g. [Line 6](docker-compose.yml#L6) -> `dockerfile: container-scripts/database/postgresql/Dockerfile`
1. `environment` defines environment variables set in the container.
    1. `database` service requires the few environment variables to start.([Line 9](docker-compose.yml#L9))
        ```
        environment:
            POSTGRES_DB: $DATABASE_NAME
            POSTGRES_USER: $DATABASE_USER
            POSTGRES_PASSWORD: $DATABASE_PASSWORD
        ```
    1. `app` service requires the few environment variables to work.([Line 25](docker-compose.yml#L25))
        ```
        environment:
            DATABASE_TYPE: $DATABASE_TYPE
            DATABASE_NAME: $DATABASE_NAME
            DATABASE_USER: $DATABASE_USER
            DATABASE_PASSWORD: $DATABASE_PASSWORD
            DATABASE_HOST: $DATABASE_HOST
            DATABASE_PORT: $DATABASE_PORT
        ```
1. `networks` defines the name of the network. This project configured both [database](docker-compose.yml#L3) and [app](docker-compose.yml#L21) services in one network. ([Line 13](docker-compose.yml#L13) and [Line 32](docker-compose.yml#L32)) 
    ```
    networks:
        - crud-net
    ```
1. `healthcheck` declares a check that runs to determine whether the service containers are "healthy".
   To determine if the `database` service is ready to accept connection a test is run. The test runs twice with an
   interval of 10s and timeout of 5s if the first run was failed. ([Line 15](docker-compose.yml#L15))
    ```
    healthcheck:
        test: ["CMD-SHELL", "sh -c 'pg_isready -U $${POSTGRES_USER} -d $${POSTGRES_DB}'"]
        interval: 10s
        timeout: 5s
        retries: 2
    ```
1. `app` service is dependent on `database` service. Therefore, the following section is
   added ([Line 34](docker-compose.yml#L34))
    ```
    depends_on:
        db:
            condition: service_healthy
    ```

1. A [`docker-compose.yml` file](docker-compose.yml) is used to build the dockerfiles.
1. For each `service` under the `build` set the `context` path (e.g. `project_directory`).
1. Also set the `Dockerfile` path.