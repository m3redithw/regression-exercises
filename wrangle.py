# Importing libraries

import pandas as pd
import env
import seaborn as sns
import requests
import os
import matplotlib.pyplot as plt

# Getting conncection to mySQL database, and acquiring data

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def new_zillow_data():
    '''
    This function reads the Zillow data from the mySQL database into a df.
    '''
    # Create SQL query.
    sql_query = '''
    SELECT 
    bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
FROM
    properties_2017;
    '''
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))
    
    return df

def get_zillow_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('zillow.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('zillow.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_zillow_data()
        
        # Cache data
        df.to_csv('zillow.csv')
        
    return df 
    
def wrangle_zillow(df):
    
    # Renaming columns
    df.rename(columns = {'bedroomcnt':'bedrooms'}, inplace = True)
    df.rename(columns = {'bathroomcnt':'bathrooms'}, inplace = True)
    df.rename(columns = {'calculatedfinishedsquarefeet':'square_feet'}, inplace = True)
    df.rename(columns = {'taxvaluedollarcnt':'tax_assessed_value'}, inplace = True)
    df.rename(columns = {'taxamount':'tax_amount'}, inplace = True)
    df.rename(columns = {'fips':'fips_code'}, inplace = True)
    df.rename(columns = {'yearbuilt':'year_built'}, inplace = True)
    
    # Converting data types
    df.year_built= df.year_built.astype('int')
    df = df.dropna()
    return df
    