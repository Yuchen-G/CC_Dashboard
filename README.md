![CHN_logo](CHN_logo.png) 

This is the dashboard created to provide inputs to CHN team.

### Usage
Note: Run Makefile to download the data required. 

**Data Sources**
<br>**API URI used for GrossRentByBedRooms metric**
<br>base_uri_gross_rent := 'https://api.census.gov/data/2019/acs/acs1'</br>

**API URI used for costBurden metric**
<br>base_uri_cost_burden := 'https://www.huduser.gov/hudapi/public/chas'</br>

**API token used for costBurdenMetric**
<br>api_token := 'Register for the API at - https://www.huduser.gov/portal/dataset/chas-api.html'</br>

<code>download: input/GrossRentByBedRooms.json input/costBurden.csv
<br>
input/GrossRentByBedRooms.json:
    python downloadGrossRent.py $(base_uri_gross_rent) input/ GrossRentByBedRooms.json


input/costBurden.csv:
	python downloadCostBurden.py $(base_uri_cost_burden) $(api_token) input/ costBurden.csv</code>