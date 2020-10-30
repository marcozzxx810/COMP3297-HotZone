# HotZone

## Description
HotZone is a full stack website, supporting management of data related to locations cluster visited by known case, to identify clusters, and to visualize the clustering result. 

## How to start the development server
```
pipenv install
python3 manage.py migrate
python3 manage.py runserver_plus   
```

## Current Limitation and Assumption
- Inside location tab, the website cannot handle the case where GeoDatastore return multiple location.
- Inside all tab, the input field for number currently not support frondend field vadiation and error message will be display after submitted.
- Current verions, all the information cannot be viewed through the HotZone site.
- After created the case, CHP staff need to remember the caseID to add location record
- Assume Virus Name is unique

## Current Avaliable Function
- To create case
- To create location record 
- To create virus 

## Depolyment
Link: https://hotzonemarcomak.herokuapp.com/