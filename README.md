# Building a CI/CD Pipeline
In this project we will build a CI-CD pipeline by using Githun Actions, Azure app services and Azure pipelines by levaraging the Continuous integration and continous delivery strategies learnt in the course.

#

## Agile Planning and Communication
For planning and organizing the ToDo tasks, we will go through Trello for day to day tasks and use google sheets for planning weekly, quaterly and yearly outlooks.

[Trello boardfor day to day tasks](https://trello.com/invite/b/eV2dTCfS/ATTIb73a021f9cc41346b085b28ba7240ac05C513744/ci-cd-2nd-project)

[Google spreadsheets for high level overview and planning](https://docs.google.com/spreadsheets/d/1i13qxWZAgimTkDBM0qaHdZdUQZiCsq8p/edit?usp=sharing&ouid=106030168383046099430&rtpof=true&sd=true)

#

## Architecture Overview

diagram



## Steps 

#### clone the Repo in Azure cloud shell
- After creating github repo we have to clone it to azure cloud shell, create ssh-keys and upload them into gitHub account.

```
git clone git@github.com:srinidhi007/2nd-project-CI-CD.git
```
- It has to look something like this:
diagram


#### Install requirements and Test
- run the make file to install all the necessary packages and test it with pylint
```
make all
```
- It will look something like this:
diagram


