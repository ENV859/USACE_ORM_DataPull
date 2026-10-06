# ORG_AGOL_Scrape.py
# This script scrapes ORM point features from the USACE ORM AGOL server
# https://geospatial.sec.usace.army.mil/regulatory/rest/services/ORM/ORM_Project_Locations_Public/FeatureServer/0
#
# John.Fay@duke.edu

#%% 
#Packages
from pathlib import Path
from arcgis import GIS
from arcgis.features import FeatureLayer, FeatureLayerCollection

gis = GIS('home')

save_folder = Path.cwd().parent / 'data' / 'raw'

#%%
# Connect to the data
the_url = 'https://geospatial.sec.usace.army.mil/regulatory/rest/services/ORM/ORM_Project_Locations_Public/FeatureServer'
the_layers = FeatureLayerCollection(url=the_url).layers

#%%
# Process the first layer
the_layer = the_layers[0]


# %%

# Get all object IDs
ids = the_layer.query(
    where="1=1",
    return_ids_only=True
)["objectIds"]

print(f"{len(ids):,} features")

batch_size = the_layer.properties.maxRecordCount

for start in range(0, len(ids), batch_size):
    batch_ids = ids[start:start + batch_size]

    fs = layer.query(
        object_ids=",".join(map(str, batch_ids)),
        out_fields="*",
        return_geometry=True
    )

    # process/save this batch here
    fs.save(
        save_location=str(save_folder),
        out_name="features.geojson"
    )

    break
# %%
