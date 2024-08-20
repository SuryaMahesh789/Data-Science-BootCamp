[cloudera@quickstart ~]$ pyspark

Python 2.6.6 (r266:84292, Jul 23 2015, 15:22:56) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [jar:file:/usr/local/spark/jars/slf4j-log4j12-1.7.16.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/lib/zookeeper/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/lib/flume-ng/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/lib/parquet/lib/slf4j-log4j12-1.7.5.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [jar:file:/usr/lib/avro/avro-tools-1.7.6-cdh5.13.0.jar!/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [org.slf4j.impl.Log4jLoggerFactory]
2024-08-18 21:10:41 WARN  Utils:66 - Your hostname, quickstart.cloudera resolves to a loopback address: 127.0.0.1; using 192.168.23.129 instead (on interface eth4)
2024-08-18 21:10:41 WARN  Utils:66 - Set SPARK_LOCAL_IP if you need to bind to another address
2024-08-18 21:10:42 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.3.1
      /_/

Using Python version 2.6.6 (r266:84292, Jul 23 2015 15:22:56)
SparkSession available as 'spark'.
>>> data=[("Java","1"),("Python","2"),("Scala","3")]
>>> df=spark.createDataFrame(data)
df.s2024-08-18 21:22:43 WARN  DomainSocketFactory:117 - The short-circuit local reads feature cannot be used because libhadoop cannot be loaded.
^CTraceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/spark/python/pyspark/sql/session.py", line 693, in createDataFrame
    jdf = self._jsparkSession.applySchemaToPythonRDD(jrdd.rdd(), schema.json())
  File "/usr/local/spark/python/lib/py4j-0.10.7-src.zip/py4j/java_gateway.py", line 1255, in __call__
  File "/usr/local/spark/python/lib/py4j-0.10.7-src.zip/py4j/java_gateway.py", line 985, in send_command
  File "/usr/local/spark/python/lib/py4j-0.10.7-src.zip/py4j/java_gateway.py", line 1152, in send_command
  File "/usr/lib64/python2.6/socket.py", line 450, in readline
    data = self._sock.recv(self._rbufsize)
  File "/usr/local/spark/python/pyspark/context.py", line 246, in signal_handler
    raise KeyboardInterrupt()
KeyboardInterrupt
>>> df=spark.createDataFrame(data)
>>> df.show
<bound method DataFrame.show of DataFrame[_1: string, _2: string]>
>>> df.show()
+------+---+                                                                    
|    _1| _2|
+------+---+
|  Java|  1|
|Python|  2|
| Scala|  3|
+------+---+

>>> from pyspark.sql import SparkSession
>>> spark = SparkSession.builder.master("local[1]") \
... .appName('SparkByExamples.com') \
... .getOrCreate()
>>> print(spark.sparkContext)
<SparkContext master=local[*] appName=PySparkShell>
>>>     print("Spark App Name : "+spark.sparkContext.appName)
  File "<stdin>", line 1
    print("Spark App Name : "+spark.sparkContext.appName)
    ^
IndentationError: unexpected indent
>>> print("Spark App Name : "+spark.sparkContext.appName)
Spark App Name : PySparkShell
>>> data2 = [("Java",1),("Scala",2),("Python",3)]
>>>     df2=spark.createDataFrame(data2)
  File "<stdin>", line 1
    df2=spark.createDataFrame(data2)
    ^
IndentationError: unexpected indent
>>>     df2.show()
  File "<stdin>", line 1
    df2.show()
    ^
IndentationError: unexpected indent
>>> data2 = [("Java",1),("Scala",2),("Python",3)]
>>> df2=spark.createDataFrame(data2)
>>> df2.show()
+------+---+                                                                    
|    _1| _2|
+------+---+
|  Java|  1|
| Scala|  2|
|Python|  3|
+------+---+

>>> from pyspark import SparkContext
>>> sc = SparkContext("local","Spark_Example_App")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/spark/python/pyspark/context.py", line 115, in __init__
    SparkContext._ensure_initialized(self, gateway=gateway, conf=conf)
  File "/usr/local/spark/python/pyspark/context.py", line 308, in _ensure_initialized
    callsite.function, callsite.file, callsite.linenum))
ValueError: Cannot run multiple SparkContexts at once; existing SparkContext(app=PySparkShell, master=local[*]) created by <module> at /usr/local/spark/python/pyspark/shell.py:45 
>>> print(sc.appName)
PySparkShell
>>> from pyspark import SparkConf , SparkContext
>>> conf = SparkConf()
>>> conf.setMaster("local").setAppName("Spark Example App")
<pyspark.conf.SparkConf object at 0xc95b90>
>>> sc = SparkContext.getOrCreate(conf)
>>> 
Traceback (most recent call last):
  File "/usr/local/spark/python/pyspark/context.py", line 246, in signal_handler
    raise KeyboardInterrupt()
KeyboardInterrupt
>>> print(sc.appName)
PySparkShell
>>> rdd = spark.SparkContext.range(1,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkSession' object has no attribute 'SparkContext'
>>> print(rdd.collect())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rdd' is not defined
>>> rdd = spark.SparkContext.range(1,5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SparkSession' object has no attribute 'SparkContext'
>>> rdd = spark.sparkContext.range(1,5)
>>> rdd.collect()
[1, 2, 3, 4]
>>> rdd = spark.sparkContext.parallelize([1,2,3,4,5,6])
>>> rdd.collect()
[1, 2, 3, 4, 5, 6]
>>> data = [('James','','Smith','1991-04-01','M',3000),
...         ('Michael','Rose','','2000-05-19','M',4000),
...         ('Robert','','Williams','1978-09-05','M',4000),
...         ('Maria','Anne','Jones','1967-12-01','F',4000),
...         ('Jen','Mary','Brown','1980-02-17','F',-1)]
>>> columns = ["firstname","middlename","lastname","dob","gender","salary"]
>>> df = spark.createDataFrame(data=data, schema = columns)
>>> df.show()
+---------+----------+--------+----------+------+------+                        
|firstname|middlename|lastname|       dob|gender|salary|
+---------+----------+--------+----------+------+------+
|    James|          |   Smith|1991-04-01|     M|  3000|
|  Michael|      Rose|        |2000-05-19|     M|  4000|
|   Robert|          |Williams|1978-09-05|     M|  4000|
|    Maria|      Anne|   Jones|1967-12-01|     F|  4000|
|      Jen|      Mary|   Brown|1980-02-17|     F|    -1|
+---------+----------+--------+----------+------+------+

>>> import pyspark
>>> from pyspark.sql import SparkSession
>>> simpleData = [("James","Sales","NY",90000,34,10000),
...               ("Michael","Sales","NY",86000,56,20000),
...               ("Robert","Sales","CA",81000,30,23000),
...               ("Maria","Finance","CA",99000,24,23000),
...               ("Roman","Finance","CA",90000,34,10000),
...               ("Scott","Finance","NY",90000,34,10000),
...               ("Jen","Finance","NY",90000,34,10000),
...               ("Jeff","Marketing","CA",90000,34,10000),
...               ("Kumar","Marketing","NY",91000,50,10000)
...             ]
>>> columns = ["Employee_Name","Department","State","Salary","Age","Bonus"]
>>> df = spark.createDataFrame(data = simpleData,schema = columns)
>>> df.printSchema()
root
 |-- Employee_Name: string (nullable = true)
 |-- Department: string (nullable = true)
 |-- State: string (nullable = true)
 |-- Salary: long (nullable = true)
 |-- Age: long (nullable = true)
 |-- Bonus: long (nullable = true)

>>> df.show()
+-------------+----------+-----+------+---+-----+
|Employee_Name|Department|State|Salary|Age|Bonus|
+-------------+----------+-----+------+---+-----+
|        James|     Sales|   NY| 90000| 34|10000|
|      Michael|     Sales|   NY| 86000| 56|20000|
|       Robert|     Sales|   CA| 81000| 30|23000|
|        Maria|   Finance|   CA| 99000| 24|23000|
|        Roman|   Finance|   CA| 90000| 34|10000|
|        Scott|   Finance|   NY| 90000| 34|10000|
|          Jen|   Finance|   NY| 90000| 34|10000|
|         Jeff| Marketing|   CA| 90000| 34|10000|
|        Kumar| Marketing|   NY| 91000| 50|10000|
+-------------+----------+-----+------+---+-----+

>>> df.show(truncate=False)
+-------------+----------+-----+------+---+-----+
|Employee_Name|Department|State|Salary|Age|Bonus|
+-------------+----------+-----+------+---+-----+
|James        |Sales     |NY   |90000 |34 |10000|
|Michael      |Sales     |NY   |86000 |56 |20000|
|Robert       |Sales     |CA   |81000 |30 |23000|
|Maria        |Finance   |CA   |99000 |24 |23000|
|Roman        |Finance   |CA   |90000 |34 |10000|
|Scott        |Finance   |NY   |90000 |34 |10000|
|Jen          |Finance   |NY   |90000 |34 |10000|
|Jeff         |Marketing |CA   |90000 |34 |10000|
|Kumar        |Marketing |NY   |91000 |50 |10000|
+-------------+----------+-----+------+---+-----+

>>> df.sort("department","state").show(truncate=False)
+-------------+----------+-----+------+---+-----+
|Employee_Name|Department|State|Salary|Age|Bonus|
+-------------+----------+-----+------+---+-----+
|Maria        |Finance   |CA   |99000 |24 |23000|
|Roman        |Finance   |CA   |90000 |34 |10000|
|Jen          |Finance   |NY   |90000 |34 |10000|
|Scott        |Finance   |NY   |90000 |34 |10000|
|Jeff         |Marketing |CA   |90000 |34 |10000|
|Kumar        |Marketing |NY   |91000 |50 |10000|
|Robert       |Sales     |CA   |81000 |30 |23000|
|James        |Sales     |NY   |90000 |34 |10000|
|Michael      |Sales     |NY   |86000 |56 |20000|
+-------------+----------+-----+------+---+-----+

>>> df.sort("department")
DataFrame[Employee_Name: string, Department: string, State: string, Salary: bigint, Age: bigint, Bonus: bigint]
>>> df.show()
+-------------+----------+-----+------+---+-----+
|Employee_Name|Department|State|Salary|Age|Bonus|
+-------------+----------+-----+------+---+-----+
|        James|     Sales|   NY| 90000| 34|10000|
|      Michael|     Sales|   NY| 86000| 56|20000|
|       Robert|     Sales|   CA| 81000| 30|23000|
|        Maria|   Finance|   CA| 99000| 24|23000|
|        Roman|   Finance|   CA| 90000| 34|10000|
|        Scott|   Finance|   NY| 90000| 34|10000|
|          Jen|   Finance|   NY| 90000| 34|10000|
|         Jeff| Marketing|   CA| 90000| 34|10000|
|        Kumar| Marketing|   NY| 91000| 50|10000|
+-------------+----------+-----+------+---+-----+

>>> from pyspark.sql import SparkSession
>>> from pyspark.sql.functions import col
>>> spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
>>> data = [
...     ("James",None,"M"),
...     ("Anna","NY","F"),
...     ("Julia",None,None)
... ]
>>> columns = ["name","state","gender"]
>>> df = spark.createDataFrame(data,columns)
>>> df.printSchema()
root
 |-- name: string (nullable = true)
 |-- state: string (nullable = true)
 |-- gender: string (nullable = true)

>>> df.show()
+-----+-----+------+
| name|state|gender|
+-----+-----+------+
|James| null|     M|
| Anna|   NY|     F|
|Julia| null|  null|
+-----+-----+------+

>>> df.createOrReplaceTempView("DATA")
>>> spark.sql("SELECT * FROM DATA where STATE IS NULL").show()
+-----+-----+------+
| name|state|gender|
+-----+-----+------+
|James| null|     M|
|Julia| null|  null|
+-----+-----+------+

>>> spark.sql("SELECT * FROM DATA where STATE IS NULL AND GENDER IS NULL").show()
+-----+-----+------+
| name|state|gender|
+-----+-----+------+
|Julia| null|  null|
+-----+-----+------+

>>> spark.sql("SELECT * FROM DATA where STATE IS NOT NULL").show()
+----+-----+------+
|name|state|gender|
+----+-----+------+
|Anna|   NY|     F|
+----+-----+------+

>>> df.filter("state is not NULL").show()
+----+-----+------+
|name|state|gender|
+----+-----+------+
|Anna|   NY|     F|
+----+-----+------+

>>> df.filter("NOT state is NULL").show()
+----+-----+------+
|name|state|gender|
+----+-----+------+
|Anna|   NY|     F|
+----+-----+------+

>>> df.filter(df.state.isNotNull()).show()
+----+-----+------+
|name|state|gender|
+----+-----+------+
|Anna|   NY|     F|
+----+-----+------+

>>> df.filter(col("state").isNotNull()).show()
+----+-----+------+
|name|state|gender|
+----+-----+------+
|Anna|   NY|     F|
+----+-----+------+

>>> df.filter("state is NULL").show()
+-----+-----+------+
| name|state|gender|
+-----+-----+------+
|James| null|     M|
|Julia| null|  null|
+-----+-----+------+

>>> df.filter("state is NULL").show()
+-----+-----+------+
| name|state|gender|
+-----+-----+------+
|James| null|     M|
|Julia| null|  null|
+-----+-----+------+

>>> df.filter(df.state.isNull()).show()
+-----+-----+------+
| name|state|gender|
+-----+-----+------+
|James| null|     M|
|Julia| null|  null|
+-----+-----+------+

>>> df.filter(col("state").isNull()).show()
+-----+-----+------+
| name|state|gender|
+-----+-----+------+
|James| null|     M|
|Julia| null|  null|
+-----+-----+------+

>>> data = [("Alice",25),("Bob",30),("Carol",35)]
>>> schema = ["name","age"]
>>> df = spark.createDataFrame(data,schema=schema)
>>> df.show()
+-----+---+
| name|age|
+-----+---+
|Alice| 25|
|  Bob| 30|
|Carol| 35|
+-----+---+

>>> df.createOrReplaceTempView("people")
>>> # select rows where age is greater than 30
... result = spark.sql("SELECT * FROM people WHERE age >30")
>>> result.show()
+-----+---+
| name|age|
+-----+---+
|Carol| 35|
+-----+---+

>>> result = spark.sql("SELECT * FROM people WHERE age <30")
>>> result.show()
+-----+---+
| name|age|
+-----+---+
|Alice| 25|
+-----+---+

>>> df.show()
+-----+---+
| name|age|
+-----+---+
|Alice| 25|
|  Bob| 30|
|Carol| 35|
+-----+---+

>>> df2.show()
+------+---+
|    _1| _2|
+------+---+
|  Java|  1|
| Scala|  2|
|Python|  3|
+------+---+

>>> data2 = [("Alice","Engineer"),("Bob","Data Scientist"),("Eve","Designer")]
>>> schema2 = ["Name","Occupation"]
>>> df2=spark.createDataFrame(data2,schema=schema2)
>>> df2.createOrReplaceTempView("occupations")
>>> result = spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
  File "<stdin>", line 1
    result = spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
                                                                                                              ^
SyntaxError: EOL while scanning string literal
>>> data2 = [("Alice","Engineer"),("Bob","Data Scientist"),("Eve","Designer")]
>>> schema2 = ["name","occupation"]
>>> df2=spark.createDataFrame(data2,schema=schema2)
>>> df2.createOrReplaceTempView("occupations")
>>> result = spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
  File "<stdin>", line 1
    result = spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
                                                                                                              ^
SyntaxError: EOL while scanning string literal
>>> df.show()
+-----+---+
| name|age|
+-----+---+
|Alice| 25|
|  Bob| 30|
|Carol| 35|
+-----+---+

>>> df2.show()
+-----+--------------+
| name|    occupation|
+-----+--------------+
|Alice|      Engineer|
|  Bob|Data Scientist|
|  Eve|      Designer|
+-----+--------------+

>>> df2.createOrReplaceTempView("occupations")
>>> result = spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
  File "<stdin>", line 1
    result = spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
                                                                                                              ^
SyntaxError: EOL while scanning string literal
>>> spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
  File "<stdin>", line 1
    spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name)
                                                                                                     ^
SyntaxError: EOL while scanning string literal
>>> result = spark.sql("SELECT p.name, p.age, o.occupation FROM people p JOIN occupations o ON p.name = o.name")
>>> result.show()
[Stage 36:=====================================================>  (19 + 1) / 20                                                                               [Stage 39:============>                                          (22 + 1) / 100[Stage 39:=================>                                     (32 + 1) / 100[Stage 39:=====================>                                 (39 + 1) / 100[Stage 39:==========================>                            (48 + 1) / 100[Stage 39:=================================>                     (60 + 1) / 100[Stage 39:=========================================>             (75 + 1) / 100[Stage 39:==================================================>    (91 + 1) / 100                                                                               [Stage 42:===================================>                    (47 + 1) / 75[Stage 42:==============================================>         (62 + 1) / 75                                                                               +-----+---+--------------+
| name|age|    occupation|
+-----+---+--------------+
|  Bob| 30|Data Scientist|
|Alice| 25|      Engineer|
+-----+---+--------------+

>>> 2024-08-19 20:29:25 WARN  HeartbeatReceiver:66 - Removing executor driver with no recent heartbeats: 58422506 ms exceeds timeout 120000 ms
2024-08-19 20:29:29 ERROR TaskSchedulerImpl:70 - Lost executor driver on localhost: Executor heartbeat timed out after 58422506 ms
2024-08-19 20:29:30 WARN  SparkContext:66 - Killing executors is not supported by current scheduler.
>>> 
