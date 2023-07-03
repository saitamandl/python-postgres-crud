# python CRUD operation
Use a database (postgresql) docker container and python app container to run a simple CRUD (Create, Read, Update and Delete) operation.

## Docker Container
1. A `Dockerfile` for the database is created e.g. [postgresql Dockerfile](container-scripts/database/postgresql/Dockerfile).
   1. `COPY` command is used to copy files from host to docker container.
      1. Source (host) path is dependent on the `context` path.
1. A [`docker-compose.yml` file](docker-compose.yml) is used to build the dockerfiles.
   1. For each `service` under the `build` set the `context` path (e.g. `project_directory`).
   2. Also set the `Dockerfile` path.
## SSL certificate
For this app we will use a **SSL** certificate for secure connection. Therefore, a **SSL** certificate is required for the local development.

To create the certificate the following command is used: 
```
 openssl req -x509 -newkey ed25519 -keyout ${project_directory}/.utils/certificates/ssl.db.key -out ${project_directory}/.utils/certificates/ssl.db.cert.pem -sha256 -days 365
```
Multiple source on the internet explained how to create self-signed **SSL** certificates e.g. [here is one explanation](https://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-22-04)
