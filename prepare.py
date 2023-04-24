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

def prepare_opsd():
    '''
    Actions: gets data, creates new columns, and drops null values
    '''
    
    # set file name
    filename = 'opsd_germany_daily.csv'

    # if the file exists
    if os.path.exists(filename):
        
        # read the csv 
        df = pd.read_csv(filename, index_col=0)
        
    
    # otherwise
    else:
        
        # get data
        df = pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')

    # creating python friendly names
    df.columns = df.columns.str.lower().str.replace('+', '_')

    # converting dates to datetime
    df.date = pd.to_datetime(df.date)

    # setting index
    df = df.set_index('date')

    # setting month
    df['month'] = df.index.month_name()

    # setting day
    df['day'] = df.index.day_name()
    
    # drop nulls
    df.dropna(inplace=True)
    
    return df