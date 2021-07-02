# Zenatix
## Zenatix Solutions Assignment - Montoring Local Machine with Elastic Search and Kibana

### 1. Clone Repository

### 2. Project Set-Up - Change to cloned directory.

```

docker-compose up

```
### 3. Check for servers up and running.

```

docker-compose ps

```

### 4. Check Kibana Server running on (http://localhost:5601)

### 5. Go to terminal and run zenatix.py

```

python zenatix.py

```

### 6. Check indices for elastic search.

```

curl -X GET "http://localhost:9200/_cat/indices?v"

```

### 7. Open Kibana Server again- Connect to index metrics and play with the dashboard.

