# TASK LIST CLI-PYTHON 
This python app use CouchDB as its database and use Fire library to run the command line interface 

# Installation

* 1st install poetry on your system https://python-poetry.org/ 
* run ``` poetry install ```
* run ``` ./task_list.sh -h ``` for available help
* example to  check available List Of task from user jhon  ``` ./task_list.sh jhon ```

# Development
This app use following library
* fire (For Command Line Utility)
* coucdb (Connector to couchdb)