import pandas as pd
import requests
import urllib.request
import json
import numpy as np
from ast import literal_eval
from config import *


class MergeFiles:
    def __init__(self):
        pass

    def merge_files(self):
        # Mergining files
        # Fetching the customer data from URL
        with urllib.request.urlopen(customers_url) as url:
            customerts_data = url.read().decode('utf-8')
        # Converting JSON to Dataframe
        customers = pd.DataFrame.from_records(json.loads('[' + customerts_data.replace('\n',',') + ']'))
        visits = pd.read_csv(visits_url)
        visits.rename(columns={'Unnamed: 0':'visit_column1'}, inplace=True)
        # Loading loans data into Dataframe.
        loans = pd.DataFrame()
        for loan_url in loans_urls:
            data = pd.read_csv(base_url + loan_url)
            loans = loans.append(data)
        # Merging customer and loans together 
        customer_loans = loans.merge(customers, left_on='user_id',right_on='id', how='left')
        # Removing the duplicate column
        customer_loans.drop('id_y', axis=1, inplace=True)
        # renaming the column names which are clashing
        customer_loans.rename(columns={'id_x':'id','Unnamed: 0':'loan_column1'}, inplace=True)
        # Merging customer, loans with visits 
        # Fill null values with 0
        customer_loans['webvisit_id'] = [literal_eval(x)[0] for x in customer_loans['webvisit_id'].fillna(str((0,)))]
        # Merging customers and loans
        final_data = customer_loans.merge(visits, left_on='webvisit_id', right_on='id', how='left')
        # Renaming the same columns in both tables
        final_data.rename(columns={'id_x':'id','timestamp_x':'loan_timestamp','id_y':'visit_id','timestamp_y':'visit_timestamp' }, inplace=True)
        # Replacing null values with 0 
        final_data['visit_column1'] = [int(x)  if str(x) != 'nan' else 0 for x in final_data['visit_column1']]
        final_data['visit_id'] = [int(x)  if str(x) != 'nan' else 0 for x in final_data['visit_id']]
        final_data['visit_timestamp'] = [int(x)  if str(x) != 'nan' else 0 for x in final_data['visit_timestamp']]
        # Saving data to merged_data.csv
        final_data.to_csv('merged_data.csv')
        return


merger_obj = MergeFiles()
merger_obj.merge_files()
