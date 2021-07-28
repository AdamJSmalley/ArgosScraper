# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy.utils.project import get_project_settings


class MySQLInsertPipeline(object):
    def __init__(self): #connect to the database which is defined in the settings file
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **get_project_settings().get('DATABASE'))
    
    def __del__(self): #disconnect from the database when finsihed
        self.dbpool.close()

    def open_spider(self, spider): #get the table the data will be stored in from the spider and save it to a variable in this class
        self.sqlquery = "INSERT INTO " + spider.table + " VALUES('{}');"
        print(self.sqlquery)

    def process_item(self, item, spider): #insert the data
        self.dbpool.runOperation(self.sqlquery.format("', '".join(item.values())))
        return item