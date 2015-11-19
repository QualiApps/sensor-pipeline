# Apache Nifi - Sensor PipeLine

This container builds a container with the
Nifi and predefined templates (Sensor and Listener).

## Running your image
--------------------------

Start your image binding extrenal ports 8080, 8088.

   docker run -d -p 8080:8080 -p 8088:8088 qapps/sensor-pipeline:master

## Docker compose yml example

```
stream:
    image: qapps/sensor-pipeline:master
    ports:
	- "8080:8080"
	- "8088:8088"
```