# program to extract tables and use numpy and pandas to manipulate te data and use matplot lib to plot charts where necessary
# as well as using loops to  iterate through a data set to identify certian elements as well  as replace
# also using numpy to perform calculations.

# first create a web scrapper
# in a class, visualize the data from the table
#  clean and prepare the data by editing headrrs, selecting relevant options
#  perform calcualtions  on certain parts of the data
# visualize the data
#  save the data to csv etc

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# soup = BeautifulSoup(res.content, 'html-parser')
# df = pd.read_html(url)
# table 2 = df[1]
# table 2 = df(2)

async def fetchApi(url):
   '''
   this function  will scrape tabular data only from any website inputed in it
   ''' 
   data = await pd.read_html(url)
   return data.content

# fetcch from the url
tables = fetchApi('google.com')





class dataManipulator(object):

    def __init__(self,tables):
        self.tables= tables
        self.selected_tables = None

    def displaydf(self,table_title):
        '''
        this function  displays the table in data frame  after extracting a particular tableand returns an output that the  next method will use
        ''' 
        topic_status_boolean = table_title in self.tables
        
        # loop through each table to search for the topic
        for index, table in enumerate(self.tables.values):
            if topic_status_boolean:
                print(f'Topic found in table {index}')
                self.selected_tables = table
                print(self.selected_tables)
                break # stops after finding the first table with the topic
        else:
            print('Topic not found in the list')

        # search the dict for a predefined topic 
        #  store the dict of the topic so that othr metods cann acess the topic
    def prepare_date(self):
        '''
        perform some operations to make data clearer
        '''
        imported_table = self.selected_tables
        pass
        # clean the data by converting column titles to wht they  should be
        # check for and remove duplicates
        # format types
    
   

    def analyze_data():
        pass
        # analyzedata
                  

        
    
      


 