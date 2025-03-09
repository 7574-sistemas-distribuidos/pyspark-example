# PySpark Example

Based on [** DeadSimple: PySpark + Docker Spark Cluster on your Lapto**](https://medium.com/programmers-journey/deadsimple-pyspark-docker-spark-cluster-on-your-laptop-9f12e915ecf4)

Showcase how to launch a Spark cluster, create a image to run pyspark pipelines, and attach it to the cluster using `docker compose`.

## Execution
- Start the Spark cluster:

```
docker compose up -d spark spark-worker
```

- Run the client worktask:

```
docker compose up client
```

- Stop the Spark cluster
```
docker compose stop
```
