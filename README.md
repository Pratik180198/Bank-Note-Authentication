# Bank-Note-Authentication

## Deploy a ML application with Streamlit and Docker on Heroku Platform

## Table of Content
  
  * [Dataset](#dataset)
  * [Overview](#overview)
  * [Demo](#demo)
  * [Screenshots](#screenshots)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Bug / Feature Request](#bug--feature-request)
  * [Technologies Used](#technologies-used)
  * [Team](#team)


## Dataset
Data Set Information:

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

Dataset extracted from: https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data

Attribute Information:
1. variance of Wavelet Transformed image (continuous)
2. skewness of Wavelet Transformed image (continuous)
3. curtosis of Wavelet Transformed image (continuous)
4. entropy of image (continuous)
5. class (integer)


## Overview
This example aims to detect fraudulent notes accurately.
For that, a set of images taken from genuine and forged banknote-like specimens is created. Features such as wavelet variance, wavelet skewness, wavelet kurtosis, and image entropy are extracted from the images.

The final accuracy obtained by this method is 100% on an independent testing set.

This is a classification project, since the variable to be predicted is binary (fraudulent or legal).
The goal here is to model the probability that a banknote is fraudulent, as a function of its features.


## Demo
Link: [https://bank-money-api.herokuapp.com/](https://bank-money-api.herokuapp.com/)


## Screenshots
<a href="url"><img src="https://github.com/Pratik180198/Bank-Note-Authentication/blob/main/Screenshots/Screenshot%20(68).png"  height="500" width="550" ></a>


## Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

For creating the ML model, [Jupyter notebook](https://jupyter.org/install) is used. For creating the web app Streamlit framework is used for running the streamlit python file run the following command in your working environment comand prompt.
```bash
streamlit run sapp.py
```
You can also follow the [streamlit documentation](https://docs.streamlit.io/en/stable/) to know more about it.

We had also developed another web app using Flask framework and Flasgger which is a Flask extension to extract OpenAPI-Specification from all Flask views registered in your API. Flasgger also comes with SwaggerUI embedded so you can access http://localhost:5000/apidocs and visualize and interact with your API resources.

We had used Docker which is a set of platform as a service (PaaS) products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels. Because all of the containers share the services of a single operating system kernel, they use fewer resources than virtual machines. Follow the steps to install [Docker](https://docs.docker.com/get-docker/). If your system does not supports docker then you can try [Docker toolbox](https://github.com/docker/toolbox/releases).

To dockerize you must create a [Dockerfile](https://github.com/Pratik180198/Bank-Note-Authentication/blob/main/Dockerfile).

The next step is to open the Docker Quickstart Terminal in your present working directory where all files and Dockerfile is present and shoot this command:

To build the Docker image 
```bash
docker build -t streamlit_app .
```

To run the Docker image:
```bash
docker run -p 8501:8501 streamlit_app
```

Instead if you have any problem you can see the [Docker Documentation](https://docs.docker.com/).

Also see the important commands for Docker provide by [DZone](https://dzone.com/articles/how-to-run-docker-container-on-your-local-machine).

The main [sapp.py](https://github.com/Pratik180198/Bank-Note-Authentication/blob/main/sapp.py) is used for deployment with Heroku.


## Deployement on Heroku
To deploy this app we are using Heroku Platform. You must first register on [Heroku](https://www.heroku.com/home).
Create your new app and give the app name and start deploying with the help of Heroku CLI command or connect your Github account.
After successful connecting search your application repository and then start your deploying process.
Once the app is successfully build you can visit your web app.

Our next step would be to follow the instruction given on [Heroku Documentation](https://devcenter.heroku.com/articles/getting-started-with-python) to deploy a web app.

The next step is that you must create [setup.sh](https://github.com/Pratik180198/Bank-Note-Authentication/blob/main/setup.sh). ‘setup.sh’ specifies the commands to be executed to configure the environment before running the app.

‘Procfile’ lists the commands to be executed to start the app. In our ‘Procfile’, we’ll first run ‘setup.sh’ that creates the required config files and then run the app using the ‘streamlit run’ command.
```bash
web: sh setup.sh && streamlit run sapp.py
```


## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/Pratik180198/Bank-Note-Authentication/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/Pratik180198/Bank-Note-Authentication/issues/new). Please include sample queries and their corresponding results.


## Technologies Used

<img alt="Python" src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white"/> 
<img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"/>
<img alt="PyCharm" src="https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green"/>
<img alt="GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"/>
<img alt="Heroku" src="https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"/>
<img alt="Pandas" src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" />
<img alt="NumPy" src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" />
<img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/>
<img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-%23F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white" />
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourGitHub)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=170>](https://scikit-learn.org/stable/) [<img target="_blank" src="https://matplotlib.org/_static/logo2_compressed.svg" width=170>](https://matplotlib.org/)  [<img target="_blank" src="https://numpy.org/images/logos/numpy.svg" width=170>](https://numpy.org/) 
 [<img target="_blank" src="https://www.docker.com/sites/default/files/d8/2019-07/horizontal-logo-monochromatic-white.png" width=170>](https://www.docker.com/)
 
 
 ## Team

[<img target="_blank" src="https://avatars.githubusercontent.com/u/72552513?v=4" width=170>](https://github.com/Pratik180198) |
-|
[Pratik Bambulkar](https://github.com/Pratik180198) |)


## Contact

You can reach me 

[<img alt="Instagram" src="![image](https://user-images.githubusercontent.com/72552513/126031289-2534f1b3-6499-4782-89f5-61764c904b2a.png)"/>](https://www.instagram.com/pratikkk______/)

