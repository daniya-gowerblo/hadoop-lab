from pyspark.sql import SparkSession
import time

def main():
    # Создаем сессию
    spark = SparkSession.builder \
        .appName("Lab2Spark") \
        .getOrCreate()

    print("Starting job...")
    start_time = time.time()

    # Чтение данных из HDFS
    df = spark.read.csv("hdfs://namenode:9000/input/dataset.csv", header=True, inferSchema=True)
    
    print(f"Data loaded. Rows: {df.count()}") # Действие count() заставит Spark прочитать данные

    # Пример простой агрегации
    result = df.groupBy("category").count()
    
    # ВАЖНО: .show() — это действие, которое запускает выполнение задачи
    result.show() 

    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.2f} seconds")

    spark.stop()

if __name__ == "__main__":
    main()