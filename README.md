
# Redis Cluster

## _Redis Cluster w/ Docker Compose & Example Python App_

Based on [https://github.com/mustafaileri/redis-cluster-with-sentinel](https://github.com/mustafaileri/redis-cluster-with-sentinel) project.

### Installation
```sh
git clone https://github.com/FatihZor/Redis-Cluster.git
cd Redis-Cluster
```

### Docker-Compose Up
```sh
docker-compose up -d --scale slave=4 --scale sentinel=3
```

### Python App Run
```sh
cd python-app
pip install -r requirements.txt
python main.py
```

