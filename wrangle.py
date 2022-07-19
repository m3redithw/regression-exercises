# Importing libraries

import pandas as pd
import env
import seaborn as sns
import requests
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

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
    
def wrangle_zillow():
    df = get_zillow_data()
    # Renaming columns
    df.rename(columns = {'bedroomcnt':'bedrooms'}, inplace = True)
    df.rename(columns = {'bathroomcnt':'bathrooms'}, inplace = True)
    df.rename(columns = {'calculatedfinishedsquarefeet':'square_feet'}, inplace = True)
    df.rename(columns = {'taxvaluedollarcnt':'tax_assessed_value'}, inplace = True)
    df.rename(columns = {'taxamount':'tax_amount'}, inplace = True)
    df.rename(columns = {'fips':'fips_code'}, inplace = True)
    df.rename(columns = {'yearbuilt':'year_built'}, inplace = True)
 
    # Dropping null values
    df = df.dropna()
    # Converting data types
    df.year_built= df.year_built.astype(int)
    
   

    # Handle outliers
    df = df[df.bathrooms <= 6]
    
    df = df[df.bathrooms <= 6]

    df = df[df.tax_assessed_value < 2_000_000]
    return df

def split(df):
    '''
    This function drops the customer_id column and then splits a dataframe into 
    train, validate, and test in order to explore the data and to create and validate models. 
    It takes in a dataframe and contains an integer for setting a seed for replication. 
    Test is 20% of the original dataset. The remaining 80% of the dataset is 
    divided between valiidate and train, with validate being .30*.80= 24% of 
    the original dataset, and train being .70*.80= 56% of the original dataset. 
    The function returns, train, validate and test dataframes. 
    '''
    train, test = train_test_split(df, test_size = .2, random_state=123)   
    train, validate = train_test_split(train, test_size=.3, random_state=123)
    
    return train, validate, test
