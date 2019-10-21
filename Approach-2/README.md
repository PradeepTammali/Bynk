This is template for building a pipe line for the bulk and streaming data loading, processing data and merging data. 

In this pipe line we have three different phases.
1. Data collection and preparation 
2. Data processing 
3. Data interpretation

The total data flow pipe line looks as below.
![Architecture](docs/bynk-data-pipeline.PNG)


# 1. Data Collection and Preparation

  # Prerequisites
  A kafka cluster for the Kafka Rest Proxy serivice to push recieved data into topics.
  
  In this phase, Kafka Rest Proxy service collect data from different URLs or sources and push it different topics. On the other end, Spark service will read the data from the topics and process them. Kafka Rest Proxy is a simple web micro service which batch loads the data from URLs specified in the config file and push them into according Kafka topics.
  
 ![Architecture](docs/restproxy_config.PNG)
  
  Kafka Rest Proxy service can also work with streaming data. Whenever, Kafka Rest Proxy service receives data from REST end points it cleans, prepares and push the data to according topic. On load, Kafka Rest Proxy service start reading the data from the URLs specified in the config file and write them to the according to the topics. Afterwards, Kafka Rest Proxy will keep on listen for the data from REST endpoints. Futher, Spark Service will process the data. 

<img src=docs/Data%20Collection.PNG width="300">

A user interface service can be deployed to send the data to Kafka Rest Proxy service to ease the process of streaming process.

# 2. Data Processing

  # Prerequisites
  A Spark cluster for the Spark Service to process the recieved data.
  
  In this phase, Spark service read the data from topics and process it. This service is written in PySpark. We can make use vast libraries of the both Spark and Python to simplify the processing of data. Data read from topics are merged together based on common column between two dataframes. The data is left joined to provide information about each loan. 
  
  <img src=docs/Data%20Processing.PNG width="300">
  
  Some of the duplicate column names are renamed and null values are filled with 0. After merging the dataframes, the data can be saved in either on to local storage or to a database. Spark will give us various libraries to storage data on to different storage systems like cassandra, mongodb, hive, etc.
