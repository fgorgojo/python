"""Prueba con SPARK
 En la máquina virtual instalamos la última version de la librería de
 SPARK ( 4.1.1), pero no es compatible con la version de python instalada en 
 la máquina anfitriona es la 3.12.10 a día de hoy ( 13/01/2026).
 Podríamos pensar en instalar otra librería de spark en el entorno virtual, 
 pero ChatGPT nos dice los siguiente:

 A día de hoy, NO existe ninguna versión estable de Spark compatible con Python 3.12

 Necesitamos instalar en la maquina anfitriona, una versión de python menor: 3.11.
 Optamos por utilizar una instalación tipo embed no instalable:python-3.11.9-embed-amd64
 descomprimiendo en c:\Install\python 3.11. No queremos instalar más de una version de python.
 Estas versiones están pensadas solo para el runtime con lo que debemos realizar algunos
 pasos más:
  - Instalamos PIP:
    - Descargamos el fichero get-pip.py ( https://bootstrap.pypa.io/get-pip.py) 
    - C:\tools\python311\python.exe get-pip.py y comprobamos con 
      C:\INstall\python311\python.exe -m pip --version
    - 
 - Tenemos que instalar parte de este entorno como un pseudo entorno virtual.
   Para ello odidificamos el fichero python311.pth
 ```
    python311.zip
    .

    # Uncomment to run site.main() automatically
    Lib
    Scritps
    import site 
```
 - Añadimos la parte de spark al python 3.11
  C:\Install\python3.11\python.exe -m pip install pyspark==4.1.1

 - Descargamos una versión de winutil.exe compatible con la distribución de hadopp que viene
 con la versión de SPARK.

 - Apuntamos el resto de la variables de entorno a cada instalación: 
 JAVA_HOME, SPARK_HOME , HADOOP_HOME ,PYSPARK_PYTHON, PYSPARK_DRIVER_PYTHON
setx JAVA_HOME=  ( no existía y la agregamos)
setx SPARK_HOME=
setx HADOOP_HOME
setx PYSPARK_PYTHON=C:\Install\python3.11\python.exe
setx PYSPARK_DRIVER_PYTHON=C:\Install\python3.11\python.exe

Tambien añadimos a la variable de entorno path, %JAVA_HOME%\bin y %SPARK_HOME%\bin

"""

from pyspark.sql.types import StructType,StructField, StringType, IntegerType
import sys
from pyspark.sql import SparkSession

# ensure PySpark worker uses the same Python and enable faulthandler for better tracebacks
python_exec = sys.executable
spark = (SparkSession.builder
         .master("local[*]")
         .appName("wspark")
         .config("spark.python.worker.faulthandler.enabled", "true")
         .config("spark.sql.execution.pyspark.udf.faulthandler.enabled", "true")
         .config("spark.pyspark.python", python_exec)
         .config("spark.pyspark.driver.python", python_exec)
         .getOrCreate())

data2 = [("James","","Smith","36636","M",3000),
    ("Michael","Rose","","40288","M",4000),
    ("Robert","","Williams","42114","M",4000),
    ("Maria","Anne","Jones","39192","F",4000),
    ("Jen","Mary","Brown","","F",-1)
  ]

schema = StructType([ \
    StructField("firstname",StringType(),True), \
    StructField("middlename",StringType(),True), \
    StructField("lastname",StringType(),True), \
    StructField("id", StringType(), True), \
    StructField("gender", StringType(), True), \
    StructField("salary", IntegerType(), True) \
  ])
 
# df = spark.createDataFrame(data=data2,schema=schema)
# df.printSchema()
# df.show(truncate=False)
path='resources/wages.csv'
df = spark.read.csv(path)
df.show()

# Read a csv with delimiter, the default delimiter is ","
df2 = spark.read.option("delimiter", ",").option("header", True).csv(path)
df2.show()