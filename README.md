# Bank-Note-Authentication

## Deploy a ML application with Streamlit and Docker on Heroku Platform

## Table of Content
  
  * [Dataset](#dataset)
  * [Overview](#overview)
  * [Demo](#demo)
  * [Screenshots](#screenshots)
  * [Installation](#installation)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Documentation](#documentation)
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

For creating the ML model, [Jupyter notebook](https://jupyter.org/install) is used. For creating the web app Streamlit framework is used and we had also developed another
web app using Flask framework and Flasgger which is a Flask extension to extract OpenAPI-Specification from all Flask views registered in your API. Flasgger also comes with SwaggerUI embedded so you can access http://localhost:5000/apidocs and visualize and interact with your API resources. 

The main sapp.py is used for deployment with Heroku
