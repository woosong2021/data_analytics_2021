# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 22:16:29 2021

@author: felth
"""
# https://www.youtube.com/watch?v=E6B3uWF-V7w
# https://www.youtube.com/watch?v=-IM3531b1XU

# import streamlit as st

# Importing the tiktok Python SDK
from TikTokApi import TikTokApi as tiktok
# Import JSON for export of data
import json
# Import data processing helper
#from helpers import process_results 
# Import pandas to create dataframes
import pandas as pd
# Import sys dependency to extract command line arguments
import sys
from playwright.sync_api import sync_playwright

def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats', 'challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    # Create blank dictionary
    flattened_data = {}
    # Loop through each video
    for idx, value in enumerate(data): 
        flattened_data[idx] = {}
        # Loop through each property in each video 
        for prop_idx, prop_value in value.items():
            # Check if nested
            if prop_idx in nested_values:
                if prop_idx in skip_values:
                    pass
                else:
                    # Loop through each nested property
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx+'_'+nested_idx] = nested_value
            # If it's not nested, add it back to the flattened dictionary
            else: 
                flattened_data[idx][prop_idx] = prop_value
                
def get_data(hashtag):
    # Get cookie data
    verifyFp = "verify_kxneenuc_UNczSXul_ua20_4cXW_9IQh_B8Cs2P"
    # Setup instance
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
    # Get data by hashtag
    trending = api.by_hashtag(hashtag)
    # Process data
    flattened_data = process_results(trending)
    # Convert the preprocessed data to a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata.csv', index=False)

get_data("")    


verifyFp = "verify_kxnebfyi_FhuzooT1_OWbu_4foJ_8XVk_kWmYvY5PiXGk"
# Setup instance
api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True, use_selenium=True, executablePath=r"C:\Users\felth\Desktop\chromedriver_win32\chromedriver")
# Get data by hashtag
trending = api.by_hashtag("christmas")         
print(trending)
                                
                
                
                

                
    
