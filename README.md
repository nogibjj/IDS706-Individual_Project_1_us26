# Continuous Integration using GitHub Actions of Python

[![Install](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/test.yml)
[![Black Formatter](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/black.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/black.yml)
[![Ruff](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/ruff.yml/badge.svg)](https://github.com/nogibjj/IDS706-Individual_Project_1_us26/actions/workflows/ruff.yml)


# Overview

##### Here is the link to access the video explaining the project and demonstrating its functionality :
   

## Code Description

#### The project structure include the following files:
		
1.Jupyter_Notebook folder  that perform descriptive statistics using polars :
	
 	  - main.ipynb which contains all the functions to perform mean, mode, median and standard deviation
 	  - test_graph.ipynb which contains a visualization function to plot count of Universities  vs mean of Industry Income Score based on location
 	  - test_main.ipynb which test and asserts the true value the function written in main.ipynb and also create a summary report


2.Python_Script performing the same descriptive statistics using Polars:

 	  - polar_stats.py which contains all the functions to perform mean, mode, median and standard deviation
 	  - test_graph.py which contains a visualization function to plot count of Universities  vs mean of Industry Income Score based on location
 	  - test_stats.py which test and asserts the true value the function written in main.ipynb and also create a summary report



3.**lib.py** file that shares the common code between the python script and jupyter notebook

					
		
4.Makefile with the following:

      - install: using requirements.txt file to install required packages

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/install.png" alt="install">
</p>

      - test: Tested by using nbval plugin for pytest
              Tested test_script.py, test_lib.py and the files in jupyter_notebook and python_script

	            
python -m py.test --nbval jupyter_notebook/*.ipynb - 
<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/test1.png" alt="install">
</p>

python -m pytest -vv --cov=lib
<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/test2.png" alt="install">
</p>


python -m pytest -vv --cov=python_script python_script/*.py
<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/test3.png" alt="install">
</p>


      - format: using black formatter and nbqa plugin for .ipynb files

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/format.png" alt="format">
</p>

      
      - lint: using ruff and nbqa plugin for .ipynb files

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/lint.png" alt="lint">
</p>	

		
5.Created GitHub Actions that performs all four Makefile commands with badges for each one in the README.md

##### Action include the general CI/CD process in test.yml file, which automatically generate the graph and markdown

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/Image/yml_actions.png" alt="yml_actions">
</p>	

### Visualization 

##### Count of top universities vs mean industry income score 

<p align="center">
  <img width="600" src="https://github.com/nogibjj/IDS706-Individual_Project_1_us26/blob/main/output_graph/visualization.png" alt="visualization">
</p>	

## CI/CD Automation files

1. requirements.txt - Contains all the required python packages
2. Makfefile - Using make to automate different parts of developing a Python project, like -
   
       1. running tests
       2. cleaning builds
       3. installing dependencies
   
   Integrating it into my routine, so can save time and avoid errors.
   
3. .github/workflows - This directory in a Python project (or any GitHub repository) is used for creating and storing GitHub Actions workflows. GitHub Actions is a continuous integration and continuous delivery                           (CI/CD) platform provided by GitHub. The workflow is triggered on pushes to the main branch. It sets up :
   
       1. Python environment
       2. Installs project dependencies
       3. Install packages
       4. Runs tests
       5. Format
       6. Linting
       
