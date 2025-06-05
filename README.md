# Aws Training

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Output](#Output)

## Introduction

This repository contains the code for accessing S3 bucket through EC2 instances.

## Prerequisites

Ensure you have the following installed on your machine:

- [Flask]
- [Git](https://git-scm.com/)
- [nginx]

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   git clone https://github.com/Sulaiha-Shameena-5175/aws-mlops-assignments

2. Create a virtual environment
   virtualenv < environment_name >

   Activate it: 
   for Windows: source < environment_name >/Scripts/activate 
   for linux: source < environment_name >/bin/activate 

3. Install the dependencies:
   pip install -r requirements.txt 

4. Run the application: 
   flask run --port=8085 --host=0.0.0.0

## Output

The below images display an api call to S3 was successful and display the files and folders with in the bucket.

![output](/assets/images/output.png)