from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BatchProcessing").getOrCreate()

df = spark.read.csv("Teen_Mental_Health_Dataset.csv", header=True, inferSchema=True)

df.show(5)

df.printSchema()
df.describe().show()

df_clean = df.dropna()

df_clean.groupBy("Gender").count().show()
df_clean.groupBy("Age").avg().show()

df_clean.write.csv("output_batch", header=True)

spark.stop()
