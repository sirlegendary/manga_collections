FROM python

# set environment variables
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN apt-get update 
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . .