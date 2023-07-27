# PredictMod
## Introduction
PredictMod is a web app created to inform physicians' decisions. PredictMod takes metagenomic gastrointestinal (GI) microbiome and electronic health record (EHR) data as input and uses a machine learning algorithm to form predictions of whether the ketogenic diet may be successful. 

The PredictMod web app was designed using Figma and implemented using VueJS. For more information on these, see the links below:

[VueJS Repository](https://github.com/vuejs/core)

[VueJS Tutorial](https://code.visualstudio.com/docs/nodejs/vuejs-tutorial)

[Figma About Page](https://www.figma.com/about/)


## Setup
#### Cloning the repository
This repository can be cloned directly using the following command: 

```
git clone https://github.com/GW-HIVE/PredictMod.git
```
#### Virtual Environment
Prepare your own virtually environment using the requirement.txt file then activate your environment.

#### Installation
Navigate to the PredictMod directory and use the following command to install the necessary dependancies

```
npm install
```

#### Running the app

Navigate to the upload-api directory and execute the following command to start the server:

```
npm start
```
Navigate to the vue-upload directory and execute the following command to start the app:
```
npm run serve
```
Now a link should appear, which you can follow to see the client side of the app

#### Open the django project
Navigate to the PredictMod directory and use the following command to start the django program

```
python manage.py runserver
```
Then visit "http://127.0.0.1:8000/upload/" on your browser. The first 2 files in EHR_predict folder are the sample input files.

### Description of Main Folders and Content

#### AppView
