# Docker Task

## Description
This repository deploy a Python application ,including python code contained in index.py .
The application is a simple, “Present BTC in USD” app that uses Flask, a small HTTP server for Python apps.


## index.py
In this module we:
* Present the Current Bitcoin Price in USD.
* Present the Average Price for the last 10 minutes. <br>
We get the data from <a href="https://www.coindesk.com/price/bitcoin/">This Website</a>

## Dockerfile
```buildoutcfg
FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./index.py
```
#### FROM:<br>
telling Docker what base image to use for the container, and implicitly selecting the Python version to use, which in this case is 3.7.  <br><br>
#### COPY:<br>
moves the application into the container image.<br><br>
#### WORKDIR:<br>
sets the working directory<br><br>
#### RUN:<br>
calling pip and pointing to the requirements.txt file.<br><br>
#### EXPOSE:<br>
exposes a port that is used by Flask.<br><br>
#### CMD:<br>
tells the container what to execute to start the application. In this case, it is telling Python to run index.py.

## requirements.txt
This file contains a list of the dependencies that the application needs to run. 

### How to use
1. Install Docker `sudo apt install docker.io -y`
2. Clone the Repository
3. build the image by running Docker build from a command line or terminal that is in the root directory of the application.
4. After it is built, you can run the image as a container.

Commands:
```
git clone 'https://github.com/assiakhateeb/btcApp.git'

cd btcApp

docker build --tag my-python-app .

docker run --name python-app -p 5000:5000 my-python-app
```

After it starts, you should be able to access the application with the url `http://localhost:5000/` <br>

![url](https://user-images.githubusercontent.com/39053503/137587882-0043c4ea-8583-426f-9b39-65267bc6ea2d.png)


## Jenkins

![Jenkins](https://user-images.githubusercontent.com/39053503/137587923-1a4464d8-57f7-47fe-9708-a72ee69573b9.png)




We create a Jenkinsfile for CI/CD that creates and pushes the generated Docker image to
Docker Hub.
### How to implement
#### 1. Go to Jenkins homepage, click on “New Item”, select “Pipeline” and enter the job name as “docker-python-app”.
#### 2. In "Pipeline SCM", add the github repository `https://github.com/assiakhateeb/btcApp.git`
#### 3. Press on "Build Now" and go to "Console Output".
#### 4. You can find your job in Dashboard. <br>

![pipeline](https://user-images.githubusercontent.com/39053503/137587957-d40366c1-d9da-4f25-b2dc-5c167aea10ed.png)

#### 5. Go to DockerHub and open docker registry, you'll see the pushed image there.

 ![docker hub](https://user-images.githubusercontent.com/39053503/137588044-5764908f-381b-4058-93da-cbccc2e317d0.png)


### Jenkinsfile
#### Pipeline explanation:
In this pipeline, We have 2 environment variables to change the registry and the credential easily. <br>
The third environment is to save docker image informations.
```    environment {
    registry = "assiakhateeb/btc_app"
    registryCredential = 'dockerhub'
    dockerImage = ''
   }
   ```
