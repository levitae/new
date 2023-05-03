
# Python On-premise with Docker

An example project to monitor nodes and browse logs of Python Flask apps deployed on Docker.

- monitor-logging:
  contains tools for monitoring and logging
- myapss:
  contains 2 simple Python Flask apps and Nginx acting as reverse  proxy
- dashboards-templates: contains templates for grafana dashboards
  


## Tech Stack

**Monitoring and Logging** 

Grafana, Prometheus, Loki, Promtail and Node Exporter

**App:** 

Python, Flask

**Server:** 

Nginx


## Installation
1. Install Docker 
2. Install Loki driver plugin
```bash
  docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```
3. Edit Docker daemon config
```bash
  sudo nano /etc/docker/daemon.json
```
4. daemon.json 
```bash
  {
    "log-driver": "loki",
    "log-opts": {
        "loki-url": "http://localhost:3100/loki/api/v1/push",
        "loki-batch-size": "400"
    }
  }
```
5. Restart Docker daemon
```bash
   sudo systemctl restart docker
```
6. Create Docker Swarm 
```bash
  sudo docker swarm init
```
7. Install monitoring and logging
```bash
  cd monitoring-logging
  sudo docker-compose up -d
```
8. Install apps
```bash
  cd ../myapps
  sudo docker stask deploy -c docker-compose.yml myapps
```
## Accessing apps and grafana

#### Access Apps

##### App 1
```http
  GET https://IP-ADDR:1111/hello
```

##### App 2
```http
  GET https://IP-ADDR:1112/hello
```

#### Grafana
```http
  http://IP-ADDR:4000
  Username/Password: admin
```

#### Adding Datasource to Grafana
```http
  http://IP-ADDR:4000/connections/your-connections/datasources
```
##### Loki
* Click add new data source
* Choose Loki >> insert URL (http://loki:3100)
* Save & test make sure no error

##### Prometheus
* Click add new data source
* Choose Prometheus >> insert URL (http://prometheus:9090)
* Save & test make sure no error

#### Adding Dashboards to Grafana
```http
  http://IP-ADDR:4000/dashboards
```
##### Node Exporter dashboard
* Click New >> Import
* Input code: 1860
* Click Load >> Import

##### Apps logs dashboard
* Click New >> Import
* Upload dashboard JSON file
* File can be found in: dashboard-templates/logs.json
* Click Import
