

# Pull base image.
FROM python:3.7
ENV PYTHONUNBUFFERED 1

# Setup linkages to code repositories and add to image

WORKDIR /var/www/propertyappraisal

#Python packages
RUN pip install Django
RUN pip install djangorestframework==3.6.3
RUN pip install markdown
RUN pip install django-filter==1.1
RUN pip install psycopg2-binary
RUN pip install requests
RUN pip install gunicorn==19.6.0
RUN pip install elasticsearch
# RUN pip install urllib
# RUN pip install bs4
# FROM python:3
# ADD WebScraping.py /
# # RUN pip install urllib
# RUN pip install requests
# RUN pip install lxml
# RUN pip install bs4
# RUN pip install urllib3
# CMD [ "python", "./WebScraping.py" ]