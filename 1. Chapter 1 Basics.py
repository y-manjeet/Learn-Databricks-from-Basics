# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
df = spark.range(10)
df.show()
print(spark.version)

# COMMAND ----------

from pyspark.sql import functions as F
data = [("A",10), ('B', 20), ('A', 30)]
df = spark.createDataFrame(data, ['key', 'val'])
df.groupBy("key").agg(F.sum('val').alias('total')).show()


# COMMAND ----------

df.show()
df.display()

# COMMAND ----------

df.createOrReplaceTempView("t")

# COMMAND ----------

# MAGIC %sql
# MAGIC select key,sum(val) from t group by key

# COMMAND ----------

dbutils.widgets.text("run_date","2026-10-06")
print(dbutils.widgets.get("run_date"))

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.secrets.get

# COMMAND ----------

