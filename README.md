#  Eurostat Tourism Data Analysis in Python
Python Project 2021 for Undergraduate course of Principles of Programming Languages and Compiler Design, University of Patras

Project created on June 2021.

## Project Creator
Christos Mpalatsouras

Computer Engineering & Informatics Student at the University of Patras.

## Project Description:

Implementation of a python script to download data from Eurostat in order to extract information about tourism in Europe from 2016-2019 for the countries of Greece and Sweden.

The extracted data will be plotted in the following requested plots.

Requested plots:
1. Nights spent at tourist accommodation establishments (Data Source: https://ec.europa.eu/eurostat/databrowser/bookmark/70974cf5-72e1-489b-b56d-092cbaa59a00?lang=en)
2. Nights spent by non-residents at tourist accommodation establishments (Data Source: https://ec.europa.eu/eurostat/databrowser/bookmark/ad9f3a06-0adc-4ffb-9a00-dadf9386c99c?lang=en)
3. Arrivals at tourist accommodation establishments (Data Source: https://ec.europa.eu/eurostat/databrowser/bookmark/ed4b2617-4f9d-44b4-84d8-83f004c060ca?lang=en)
4. Arrivals of non-residents at tourist accommodation establishments (Data Source: https://ec.europa.eu/eurostat/databrowser/bookmark/a2079f11-e948-4318-b543-bd1f630524ed?lang=en)

## Project Implementation
A short description about the implementation of this project.

Project Main Application code file in Python: Implementation/main.py (https://github.com/takis104/Eurostat-Tourism-Data-Analysis-in-Python/blob/main/Implementation/main.py)

### Data downloading from the Internet
All the requested data are downloaded in Microsoft Excel format from the above links, with the requests module in Python.
Download links are valid only for a short time interval. They must be refreshed for the download process to be working correctly.

### Processing the downloaded data
For the purposes of processing the downloaded data, the "read_excel_data()" function in the application code was implemented.
The Python module "openpyxl" is being used, in order to extract the useful information from the downloaded MS Excel files.
All the useful extracted information is saved as an object of the "Dataset" class in code.

### Plotting the data
The Python Module "matplotlib" is being used to create the requested plots.

### Data storage in Database
The useful extracted info is stored in a mySQL Database, named "python_project_2021".

### Data storage in CSV files
For the purposes of extracted data storage in CSV files, the Python Module "csv" is being used.
