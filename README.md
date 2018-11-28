#  Omaha-Real Estate-WebScraping Software
This project will scrap data from county websites in Omaha  and store them in Elastic Search. Project also contains UI customized for Extracting Data from ES. 
The goal of this project is to scrap information from https://apps.sarpy.com/sarpyproperty/salesresults.aspx every day around 12:10 AM, and store the data in Elastic search (ES). In Elastic Search Document will be indexed based on every day.  The project aims to gather data from county websites, store them in ES. The project also consist of a UI designed using Ember JS, UI will be used by user or appraiser to access information and customize dashboard to retrieve information from ES.  

## Installation
cd 
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

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
