import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.master("local[*]").appName("test").getOrCreate()

df = spark.read.option("header, true").csv("data/steam_reviews.csv")
