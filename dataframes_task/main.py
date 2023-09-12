from pprint import pprint
from pyspark.sql import SparkSession, DataFrame

import os
os.environ["PYSPARK_PYTHON"]="python"

spark = SparkSession.builder.appName("dataframes_task").getOrCreate()

categories = spark.createDataFrame([
    (1, "Electronics"),
    (2, "Books"),
    (3, "Clothing"),
    (4, "For kids"),
    (5, "Home & Kitchen"),
    (6, "Sports"),
    (7, "Automotive"),
    (8, "Beauty")
], ["id", "category_name"])

products = spark.createDataFrame([
    (1, "Laptop", 1000),
    (2, "Fairy tales", 30),
    (3, "Crocs", 200),
    (4, "Coffee Maker", 80),
    (5, "Football", 25),
    (6, "Car Oil", 45),
    (7, "Lipstick", 15),
    (8, "Toy Car", 20),
    (9, "Cookbook", 10),
    (10, "Tennis Racket", 55),
    (11, "Table", 300)
], ["id", "product_name", "price"])

product_x_categories = spark.createDataFrame([
    (1, 1),
    (2, 2),
    (2, 4),
    (3, 3),
    (4, 1),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 8),
    (8, 4),
    (9, 2),
    (9, 5),
    (10, 6)
], ["product_id", "category_id"])

def get_product_x_category() -> DataFrame:
    return products.join(product_x_categories, products.id == product_x_categories.product_id, how='left') \
                   .join(categories, product_x_categories.category_id == categories.id, how='left') \
                   .select(['product_name', 'category_name'])

if __name__ == "__main__":
    get_product_x_category().show()
