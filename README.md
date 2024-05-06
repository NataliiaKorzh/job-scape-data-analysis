# job-scape-data-analysis

This project is a tool for scraping info about python-developer's vacancies and making analysis of most popular technologies on work.ua.

# How install it?
You need clone this repository to your machine.

Open project in PyCharm

Create venv for your project and install requirements
```shell
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
Command to get current info
```shell
scrapy crawl vacancies -O vacancies.csv 
```

Command to get data analysis of technologies
```shell
python vacancies_analysis.py
```
You get bar plot like this

![Plot (06.05.24)](Figure.png)