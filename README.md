#  Omaha-Real-Estate-WebScrapping
This project will scrap data from county websites in Omaha  and store them in Elastic Search. Project also contains UI customized for Extracting Data from ES. 
The goal of this project is to scrap information from https://apps.sarpy.com/sarpyproperty/salesresults.aspx every day around 12:10 AM, and store the data in Elastic search (ES). In Elastic Search Document will be indexed based on every day.  The project aims to gather data from county websites, store them in ES. The project also consist of a UI designed using Ember JS, UI will be used by user or appraiser to access information and customize dashboard to retrieve information from ES.  

## Installation
docker-compose build
docker-compose up
docker-compose run django bash
python manage.py migrate
python manage.py createsuperuser

## Getting Started
To run Omaha-Real-Estate-WebScrapping simply,
docker-compose up

# License
MIT License
Copyright (c) 2018 Sriram Srinivasan
