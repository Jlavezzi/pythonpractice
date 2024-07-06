# i will be using pandas and numpy to fetch data and manipukate them

import pandas as pd
import numpy as np
class FDI_EXTRACTOR(): 
    def __init__(self):
        self.url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

    def fetch_table(self):
        '''
        this function fetches thhe table from the url and converts it to data frames and save as csv as well pick the top 10 coutriies with the hoihghest fdis
        ''' 
        data = pd.read_html(self.url)   
        #pick the particular table with the fdi data
        fdi_df= data[3]
        
        # Replace the column headers with column numbers
        fdi_df.columns = range(fdi_df.shape[1])

        specific_data = fdi_df[[0, 4]]
        
        # pickthe top 20
        specific_data = specific_data.iloc[1:21:] 
       
        # RENAME COLUNMS
        specific_data.columns = ['Country', 'FDI (in million dollars)']
        print(specific_data)


extract =FDI_EXTRACTOR()
extract.fetch_table()      