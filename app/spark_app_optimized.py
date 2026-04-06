from pyspark.sql import SparkSession
from pyspark import StorageLevel  # Важно: импортируем StorageLevel
import time

def main():
    # Создаем сессию с настройками ресурсов
    spark = SparkSession.builder \
        .appName("Lab2SparkOptimized") \
        .config("spark.executor.memory", "1g") \
        .config("spark.driver.memory", "1g") \
        .config("spark.default.parallelism", "4") \
        .config("spark.sql.shuffle.partitions", "4") \
        .getOrCreate()

    print("Starting optimized job...")
    start_time = time.time()

    # Чтение данных из HDFS
    df = spark.read.csv("hdfs://namenode:9000/input/dataset.csv", header=True, inferSchema=True)
    
    # Оптимизация 1: Репартиционирование данных для равномерной нагрузки
    df = df.repartition(4)
    
    # Оптимизация 2: Кэширование DataFrame в памяти
    # Используем правильный объект StorageLevel
    df.persist(StorageLevel.MEMORY_AND_DISK)

    # Пример агрегации (действие, которое запускает вычисления)
    result = df.groupBy("category").count()
    
    # Действие show() для вывода результатов
    result.show() 

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

    # Очистка кэша после использования
    df.unpersist()
    
    spark.stop()

if __name__ == "__main__":
    main()