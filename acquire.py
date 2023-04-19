import math

import pandas as pd
import numpy as np

import requests

import os


def get_api_page(url, keys=True):
    '''
    Accesses an api and returns tha data in a dictionary 
    '''
    # get response from url
    response = requests.get(url)
    
    # convert response into dictionary
    data = response.json()
    
    if keys==True:
        # get the keys 
        print(data.keys())
    
    # if keys is not True
    else:
        
        # move on
        pass

    # exit function and return the data in a dictionary
    return data

def get_starwars_people():
    '''
    Returns a dataframe with all people from the starwars api people pages
    '''
    # set file name
    filename = 'people.csv'

    # if the file exists
    if os.path.exists(filename):
        
        # read the csv 
        df = pd.read_csv(filename, index_col=0)
        
        # return the df
        return df
    
    # otherwise
    else:
        # get the data as a dictionary
        data = get_api_page('https://swapi.dev/api/people/', keys=False)

        # converts the results tab into a datframe
        df = pd.DataFrame(data['results'])

        # calculates the number of people
        number_of_people = data['count']

        # determines the number of results on one page
        number_of_results = len(data['results'])

        # determins that maximum number of pages from the api
        max_page = math.ceil(number_of_people / number_of_results)

        # intiailizes a loop for each page excluding the page already used as the base
        for i in range(1, max_page):

            # stores the api response in a variable
            response = requests.get(data['next'])

            # turns the api response into a dictionary
            data = response.json()

            # adds the results from the new page to the original datarame 
            df = pd.concat([df, pd.DataFrame(data['results'])])

        # resets the index
        df = df.reset_index()

        # drop extra index column
        df.drop(columns='index', inplace=True)

        # save the df as a csv
        df.to_csv(filename)
        
    # returns the dataframe
    return df

def get_starwars_planets():
    '''
    Returns a dataframe with all planets from the starwars api planets pages
    '''
    # set file name
    filename = 'planets.csv'

    # if the file exists
    if os.path.exists(filename):
        
        # read the csv 
        df = pd.read_csv(filename, index_col=0)
        
        # return the df
        return df
    
    # otherwise
    else:

        # get the data as a dictionary
        data = get_api_page('https://swapi.dev/api/planets/', keys=False)

        # converts the results tab into a datframe
        df = pd.DataFrame(data['results'])

        # calculates the number of people
        number_of_people = data['count']

        # determines the number of results on one page
        number_of_results = len(data['results'])

        # determins that maximum number of pages from the api
        max_page = math.ceil(number_of_people / number_of_results)

        # intiailizes a loop for each page excluding the page already used as the base
        for i in range(1, max_page):

            # stores the api response in a variable
            response = requests.get(data['next'])

            # turns the api response into a dictionary
            data = response.json()

            # adds the results from the new page to the original datarame 
            df = pd.concat([df, pd.DataFrame(data['results'])])

        # resets the index
        df = df.reset_index()

        # drop extra index column
        df.drop(columns='index', inplace=True)
        
         # save the df as a csv
        df.to_csv(filename)

    # returns the dataframe
    return df


def get_starwars_starships():
    '''
    Returns a dataframe with all starships from the starwars api starships pages
    '''
    # set file name
    filename = 'starships.csv'

    # if the file exists
    if os.path.exists(filename):
        
        # read the csv 
        df = pd.read_csv(filename, index_col=0)
        
        # return the df
        return df
    
    # otherwise
    else:
    
        # get the data as a dictionary
        data = get_api_page('https://swapi.dev/api/starships/', keys=False)

        # converts the results tab into a datframe
        df = pd.DataFrame(data['results'])

        # calculates the number of people
        number_of_people = data['count']

        # determines the number of results on one page
        number_of_results = len(data['results'])

        # determins that maximum number of pages from the api
        max_page = math.ceil(number_of_people / number_of_results)

        # intiailizes a loop for each page excluding the page already used as the base
        for i in range(1, max_page):

            # stores the api response in a variable
            response = requests.get(data['next'])

            # turns the api response into a dictionary
            data = response.json()

            # adds the results from the new page to the original datarame 
            df = pd.concat([df, pd.DataFrame(data['results'])])

        # resets the index
        df = df.reset_index()

        # drop extra index column
        df.drop(columns='index', inplace=True)
        
         # save the df as a csv
        df.to_csv(filename)

    # returns the dataframe
    return df

def get_starwars_data():
    '''
    Acquires data about starships, people, and planets from starwars using an api
    '''
    
    # concat the dataframes together
    df = pd.concat([get_starwars_people(), get_starwars_planets(), get_starwars_starships()])
    
    return df
