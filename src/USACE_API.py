# USACE_API.py
# Script to scrape data using the USACE APIs:

# * https://permits.ops.usace.army.mil/orm-public-api/permits/search?
#   da=true&
#   max=25&
#   start=0&
#   q=*:*%20AND%20org:SAW%20AND%20vdate:[20250101%20TO%2020250128]&
#   bbox=-111.97265625000001,20.797201434307,-88.02246093750001,47.100044694025215



# * https://permits.ops.usace.army.mil/orm-public-api/data/hb_all_25k.json

# %%
# Packages
from pathlib import Path
import requests
import pandas as pd

# %%
# Explore API #1
the_url = 'https://permits.ops.usace.army.mil/orm-public-api/permits/search?'
the_year = 2025
params = {
    'da':'true',
    'max':1000,
    'start':0,
    'q':f'*:* AND org:SA? AND vdate:[{the_year}0101 TO {the_year}1231]',
    'bbox':'-111.97265625000001,20.797201434307,-88.02246093750001,47.100044694025215'
}

#the_url = 'https://permits.ops.usace.army.mil/orm-public-api/permits/search?da=true&max=25&start=0&q=*:*%20AND%20org:SAW&bbox=-111.97265625000001,20.797201434307,-88.02246093750001,47.100044694025215'
response = requests.get(the_url,params=params)
# %%
response_dict = response.json()
response_count = response_dict['total']
features = response_dict['results']['features']
print(f'{response_count} features returned')
# %%
dfs = []
for i, the_feature in enumerate(features):
    the_props = the_feature['properties']
    dfs.append(pd.DataFrame(the_props,index=[i]))
df_all = pd.concat(dfs)

# %%
