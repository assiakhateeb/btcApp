# set base image (host OS)
FROM python:alpine3.7
# copy the content of the local directory to the working directory /app
COPY . /app
WORKDIR /app
# install dependencies
RUN pip install -r requirements.txt
EXPOSE 5000
# command to run on container start
CMD python ./index.py