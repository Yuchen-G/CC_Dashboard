download: input/GrossRentByBedRooms.json input/costBurden.csv

input/GrossRentByBedRooms.json:
	python downloadGrossRent.py input/ GrossRentByBedRooms.json
    
input/costBurden.csv:
	python downloadCostBurden.py input/ costBurden.csv
    
