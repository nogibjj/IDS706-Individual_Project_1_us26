# Individual Project - 1

[![Install](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/test.yml)
[![Black Formatter](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/black.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/black.yml)
[![Ruff](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/ruff.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/ruff.yml)

### Creating  a Python GitHub template

## Overview



## Code Description



## CI/CD Automation files

1. requirements.txt - Contains all the required python packages
2. Makfefile - Using make to automate different parts of developing a Python project, like -
   
       1. running tests
       2. cleaning builds
       3. installing dependencies
   
   Integrating it into my routine, so can save time and avoid errors.
   
5. .github/workflows - This directory in a Python project (or any GitHub repository) is used for creating and storing GitHub Actions workflows. GitHub Actions is a continuous integration and continuous delivery                           (CI/CD) platform provided by GitHub. The workflow is triggered on pushes to the main branch. It sets up :
   
       1. Python environment
       2. Installs project dependencies
       3. Install packages
       4. Runs tests
       5. Format
       6. Linting
       
