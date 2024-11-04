from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("hellopyspark").getOrCreate()

sparkSession.createDataFrame([(1, "Shawn"), (2, "Sam")], ["id", "value"]).show()
