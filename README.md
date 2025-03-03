# Test Pipeline

## 📌 Project Overview

The pipeline follows these steps:

1. **Raw data** (dirty data) is stored in `sample-data.json`.
2. **A Python script (****`task-1.py`****)** reads this data and sends it to Kafka brokers.
3. **Logstash (****`logstash.conf`****)** processes and transforms the data before sending it to **Elasticsearch**.
4. **Kibana** is used for visualization.
5. The entire setup runs using **Docker Compose (****`docker-compose.yml`****)**.

---

## 📂 Project Structure

### 🔹 `sample-data.json`

- This file contains the **initial raw data** that will be sent to **Kafka** using a Python script.
- The data is structured in **JSON format** but contains inconsistencies (dirty fields) that need cleaning.

### 🔹 `task-1.py`

- This is the **Kafka producer script** that sends data from `sample-data.json` to Kafka.
- Uses the `confluent_kafka` Python package for Kafka interaction.
- **Waits for Kafka and Logstash to be ready** before sending data.
- **Waits an additional 30 seconds** after Kafka is ready to ensure Logstash connections are established.

### 🔹 `requirements.txt`

- Lists the required Python packages:
  ```txt
  confluent_kafka
  ```


### 🔹 `Dockerfile`

- Defines the **build instructions** for the Kafka producer script container.
- Installs required dependencies and runs `task-1.py` automatically when the container starts.
  ```sh
  pip install -r requirements.txt
  ```

### 🔹 `logstash.conf`

- **Logstash pipeline configuration** that:
  - Reads messages from Kafka.
  - Cleans and transforms the data.
  - Sends the processed data to Elasticsearch.

### 🔹 `docker-compose.yml`

- Defines the **Docker services** required for the project.
- Includes **Kafka, Zookeeper, Logstash, Elasticsearch, Kibana, and the Kafka producer script**.
- **Ensures Kafka and Logstash are ready before sending data**.

### 🔹 `kibana-discovery.png`

- A **sample Kibana screenshot** showing that the pipeline successfully processed and ingested data.

---

## 🚀 How to Run the Project

1. **Build and start all services**:

   ```sh
   docker-compose up --build -d
   ```

2. **Check Kafka topics**:

   ```sh
   docker exec -it lifeweb-kafka-1 kafka-topics --list --bootstrap-server kafka:9092
   ```

3. **View data in Elasticsearch**:

   ```sh
   docker exec -it lifeweb-elasticsearch-1 curl -X GET "http://localhost:9200/_cat/indices?v"
   ```

4. **Open Kibana at**:

   - [http://localhost:5601](http://localhost:5601)

