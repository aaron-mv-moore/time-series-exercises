# imports
import pandas as pd

import os


# function

def prepare_items():
    '''
    Actions: gets data and prepares data for exploration
    '''
    # get data
    df = pd.read_csv('tsa_item_demand.csv')
    
    # converting date to date_time format
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    
    # setting index tot he datetime
    df = df.set_index('sale_date').sort_index()
    
    # adding new columns
    df['month_name'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    df['sales_total'] = df['sale_amount'] * df['item_price']
    
    return df