# Argos Scraper

A scrapy project to scrape product information from Argos.co.uk

## Description

This scrapy project uses a custom spider to scrape product data from Argos. It scrapes the URL, price name and product categories. It stores the scraped data in a MySQL database.

## Getting Started

### Dependencies

* Python 3.6+
* [Scrapy](https://scrapy.org/)

### Installing

* [Install Scrapy](https://github.com/scrapy/scrapy)\
`pip install scrapy`
* Clone the repository.\
`git clone https://github.com/AdamJSmalley/ArgosScraper.git`

### Executing program

* Open "settings.py". Change the database setting, starting on line 93, to reflect the database you want the scraped data to be stored in.
```
DATABASE = {    
    'db': 'DATABASE',
    'user': 'USERNAME',
    'passwd': 'PASSWORD',
    'host': 'SERVER',
    'charset': 'utf8',    
    'use_unicode': True,    
}
```

## Authors

Adam Smalley - adamjs16@gmail.com

## Version History

* 0.1
    * Initial Release
