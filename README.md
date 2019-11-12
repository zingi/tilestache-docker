# tilestache-docker
Serve a tilestache server from a docker container.

## Start container with a docker-compose.yml file:
```yaml
version: '3'
services:
  tilestache:
    container_name: tilestache-server
    image: zingi/tilestache:1.0.0
    restart: unless-stopped
    ports:
     - '8181:8080' # host:container
    volumes: 
      - /path/to/local/tilestache.cfg:/etc/tilestache/tilestache.cfg
```
* Put this content in a file called **docker-compose.yml** in a folder named like **tilestache**.
* `cd` into that folder and start the container with: `docker-compose up -d`
* To check if the container is running: `docker ps`
* To follow the logs of the container: `docker logs --follow tilestache-server`
* To stop the container (being in the tilestache folder): `docker-compose down`