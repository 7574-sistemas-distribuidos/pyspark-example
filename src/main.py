import os
from pyspark.sql import SparkSession

PYSPARK_URI = os.environ.get('PYSPARK_URI', 'spark://spark:7077')

def main():
    print(f'action:connect-pyspark | result:in_progress | pyspark_uri:{PYSPARK_URI}')
    spark = SparkSession.builder \
        .appName("TestApp") \
        .master(PYSPARK_URI) \
        .getOrCreate()
    print(f'action:connect-pyspark | result:success | pyspark_uri:{PYSPARK_URI}')

    print(f'action:run | result:in_progress')
    numbers = spark.sparkContext.parallelize(range(1, 1000))
    numbers_qty = numbers.count()
    numbers_sum = numbers.sum()
    print(f'action:run | result:success | numbers_qty:{numbers_qty} | numbers_sum:{numbers_sum}')
    spark.stop()


if __name__ == "__main__":
    main()

