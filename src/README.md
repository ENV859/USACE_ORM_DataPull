# USACE ORM Data Pull
This workspace pulls data from the US Army Corp of Engineers (USACE) dataset of ORM site locations. 

The ORM is the U.S. Army Corps of Engineers' national database used to track and manage regulatory permit applications, jurisdictional determinations, and aquatic resource impacts. Publicly available data and permit tracking tools can be accessed through the USACE Regulatory and Section 408 Publicly Available Data portal.

Data are publicly available here: https://permits.ops.usace.army.mil/orm-public. 

The API is:
```
https://permits.ops.usace.army.mil/orm-public-api/permits/search?  
da=true&
max=25&
start=0&
q=*:* AND org:SA? AND vdate:[20250101 TO 20251231]&
bbox=-128,20,-70,48
```

https://permits.ops.usace.army.mil/orm-public-api/data/hb_all_25k.json

An AGOL Endpoint is: https://geospatial.sec.usace.army.mil/regulatory/rest/services/ORM/ORM_Project_Locations_Public/FeatureServer/0

https://permits.ops.usace.army.mil/orm-public-api/permits/search?da=true&max=25&start=0&q=*:*%20AND%20org:SA?%20AND%20vdate:[20260101%20TO%2020261231]&bbox=-127.74902343750001,20.59165212082918,-72.29003906250001,47.279229002570844