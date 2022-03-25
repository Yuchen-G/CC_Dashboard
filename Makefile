# variables declared for GrossRentByBedRooms metric
base_uri_gross_rent := 'https://api.census.gov/data/2019/acs/acs1'

# variables declared for costBurden metric
base_uri_cost_burden := 'https://www.huduser.gov/hudapi/public/chas'
api_token := 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjliODAyYjM0YWY2ZmJlMGUwYjlmZjZkZTMyNWRhM2M0MjNmNTgzZGFjYjcwM2JkZjdjNzAzMGEyZTIyNDRjODUxODlkZDQzNmMxYTY1MmIxIn0.eyJhdWQiOiI2IiwianRpIjoiOWI4MDJiMzRhZjZmYmUwZTBiOWZmNmRlMzI1ZGEzYzQyM2Y1ODNkYWNiNzAzYmRmN2M3MDMwYTJlMjI0NGM4NTE4OWRkNDM2YzFhNjUyYjEiLCJpYXQiOjE2NDMzMDgwNTIsIm5iZiI6MTY0MzMwODA1MiwiZXhwIjoxOTU4ODQwODUyLCJzdWIiOiIyOTM0MCIsInNjb3BlcyI6W119.IR0_v5Z4OrNawpOC3h-m33f1N_PNvKX539pehlrCLrMlCy3eJ5HDL7ddVCViUPiHe3arVJchTmqa7RO-Fc92-A'

# dependencies to run
download: input/GrossRentByBedRooms.json input/costBurden.csv

input/GrossRentByBedRooms.json:
	python downloadGrossRent.py $(base_uri_gross_rent) input/ GrossRentByBedRooms.json
    
input/costBurden.csv:
	python downloadCostBurden.py $(base_uri_cost_burden) $(api_token) input/ costBurden.csv
    
