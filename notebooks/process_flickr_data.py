# Databricks PySpark Notebook
from pyspark.sql.functions import explode, col
df = spark.read.json("/dbfs/FileStore/flickr/flickr_patents_2020.json")

# Flatten JSON, extract title/image/date
images = df.select(explode("items").alias("item"))
cleaned = images.select(
    col("item.title").alias("title"),
    col("item.link").alias("url"),
    col("item.published").alias("timestamp")
)

cleaned.write.format("delta").mode("overwrite").saveAsTable("silver_flickr_patents")
