# Airflow-Intro

This repository has the code for the Airflow Intro course with practical and basic examples. The Airflow instance is run in a Docker compose instance (See the YAML files).

Resource 1: [The Complete Hands-On Introduction to Apache Airflow](https://www.udemy.com/course/the-complete-hands-on-course-to-master-apache-airflow/).
Resource 2: [Apache Airflow: The Hands-On Guide](https://www.udemy.com/course/the-ultimate-hands-on-course-to-master-apache-airflow/)

### Developers:

* If you want to play with the code you could clone the whole repository to your local machine by:

    * `git clone https://github.com/JohnMasapantaPozo/Airflow-Intro.git`
 
* Once you have cloned the repository, you will need to initiate the docker compose instance on your machine.

    * Initiate your docker instance:
      * '-f \docker-compose-yaml up -d'
      * OR '-f \docker-compose.yaml up -d' depending on the docekr instance to initiate.
    
    * Terminate your cocker instance:
      * 'docker-compose down'
    
    *Check healthiness of your docker instance
      * '-f .\docker-compose.yaml ps'
    
    * Open you local host 8080 port 'http://localhost:8080' and loging to the Airflow instance
      * USER_NAME: airflow
      * USER_PASSWORD: airflow
