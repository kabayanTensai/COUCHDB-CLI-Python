# TASK LIST CLI-PYTHON 
This python app use CouchDB as its database and use Fire library to run the command line interface.
This python apps support Synchronize local data & online data (Couchdb) but because there's now way to support pouchdb (even tough there's lib for that but it need some other library like qwebkit) I wrote my own logic for offline Data , I store offline data on JSON file with format
``` task_list_<username>.json``` 

# How To run via docker
* run ``` docker pull danztensai123/task_list_couchdb ```
* run ``` docker run task_list_couchdb list_task john ```
# Installation & How to run

* 1st install poetry on your system https://python-poetry.org/ 
* run ``` poetry install ```
* run ``` ./task_list.sh -h ``` for available help
* example to  check available List Of task from user jhon  ``` ./task_list.sh jhon ```

## Available command for this app
To List available task from user ``` list_task  --username=<username> --mode=<online/offline>```
To Update/Create new Task ``` update_task  --username=<username --data=<dict>```
To sync between online & local data ``` sync ```

# Development
This app use following library
* fire (For Command Line Utility)
* coucdb (Connector to couchdb)