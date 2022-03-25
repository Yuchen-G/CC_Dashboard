![CHN_logo](CHN_logo.png) 

This is the dashboard created to provide inputs to CHN team.

### Usage
Note: Run Makefile to download the data required. 

<code>
download: input/GrossRentByBedRooms.json input/costBurden.csv
input/GrossRentByBedRooms.json:
	python downloadGrossRent.py $(base_uri_gross_rent) input/ GrossRentByBedRooms.json    
input/costBurden.csv:
	python downloadCostBurden.py $(base_uri_cost_burden) $(api_token) input/ costBurden.csv </code>    