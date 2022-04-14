![CHN_logo](CHN_logo.png) 

This is the dashboard created to provide inputs to CHN team.

### Usage - Metric 1 - Gross Rent Burden

**County for which chart needs to be generated**
<br>county := 'Wayne County'</br> (Choose 3 counties maximum)

**Data Sources**
<br>**ACS 1 Year Survey 2019**
<br>assets/ACSDT1Y2019.B25070-2022-01-21T214228.csv</br>

**dependencies to run**
<code>
visualization local display: 
	python streamlit run scripts/Gross_Rent_Yuchen.py </code>


### Usage - Metric 2 - Income needed to afford Fair Market Rent (FMR)

**County for which chart needs to be generated**
<br>county := 'Wayne County'</br> (Choose 3 counties maximum)

**Data Sources**
<br>**NLIHC Out of Reach 2021**
<br>assets/mi_2021_oor_data.xlsx</br>

**dependencies to run**
<code>
visualization local display: 
	python streamlit run scripts/metric_2.py </code>
	

### Usage - Metric 3 - Demographic Analysis (Race and Ethnicity)
Note: Run script to download the data required from the API's. 

**County for which chart needs to be generated**
<br>county := 'Wayne County, Oakland County, Macomb County'</br>

**Data Sources**
<br>**API URL used for Race Population Count**
<br>base_url_race : "http://api.census.gov/data/2020/dec/pl"</br>

<br>**API URL used for Ethnic Population Count**
<br>base_url_race : "http://api.census.gov/data/2020/dec/pl"</br>

**dependencies to run**
<code>
visualization local display: 
	python streamlit run scripts/demographic_analysis.py </code>
	
**downloads required datasets for both the metrics(race and ethnicity)**
<code>
assets/RacePopCount.json:
assets/EthnicPopCount.json</code>



### Usage - Metric 4
Note: Run Makefile to download the data required. 

**County for which chart needs to be generated**
<br>county := 'Wayne County'</br>

**Data Sources**
<br>**API URI used for GrossRentByBedRooms metric**
<br>base_uri_gross_rent := 'https://api.census.gov/data/2020/acs/acs5'</br>

**API URI used for costBurden metric**
<br>base_uri_cost_burden := 'https://www.huduser.gov/hudapi/public/chas'</br>

**API token used for costBurdenMetric**
<br>api_token := 'Register for the API at - https://www.huduser.gov/portal/dataset/chas-api.html'</br>

**dependencies to run**
<code>
visualization: transformCostBurden transformGrossRentByBedroom
	python visualization.py assets/ $(county) cost_burden_income.csv cost_burden_tenure.csv cost_burden_income.html cost_burden_tenure.html</code>

**creates transformed data from downloaded datasets**
<code>
transform: transformCostBurden transformGrossRentByBedroom

transformCostBurden: assets/costBurden.csv
	python transform_costBurden.py assets/ costBurden.csv cost_burden_income.csv cost_burden_tenure.csv
    
transformGrossRentByBedroom: assets/GrossRentByBedRooms.json
	python transform_grossRentByBedrooms.py assets/ GrossRentByBedRooms.json gross_rent_est.csv</code>

**downloads required datasets for both the metrics(cost_burden and gross_rent_by_bedrooms)**
<code>
assets/costBurden.csv:
	python downloadCostBurden.py $(base_uri_cost_burden) $(api_token) assets/ costBurden.csv

assets/GrossRentByBedRooms.json:
	python downloadGrossRent.py $(base_uri_gross_rent) assets/ GrossRentByBedRooms.json</code>
