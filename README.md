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
<a href="url"><img src="https://github.com/Pratik180198/Bank-Note-Authentication/blob/main/Screenshots/Screenshot%20(68).png" align="left" height="500" width="450" ></a>


