## This code appends the values of a one-column CSV file with a header to a geojson file. 
## Both files should have the same number of elements. 

## Usage: python add_csv_to_geojson.py csvfile.csv geojsonfile.json

import json
import copy
import csv
import sys


def read_in_csv(csvfile):
	with open (csvfile, 'rb') as f:
		reader = csv.reader(f)
		next(reader, None)
		properties = list(reader)
		flatlist_properties = [x for y in properties for x in y]
	return flatlist_properties

def append_properties_to_geojson(csvfile, geojsonfile):
	data = json.loads(open(geojsonfile).read())
	data = copy.deepcopy(data)
	values_to_add = read_in_csv(csvfile)
	try:
		for entry in range(len(data["features"])):
			data["features"][entry]["properties"]["value"] = values_to_add[entry]
	except:
		print "Note: Your CSV and geojson features do not contain the same number of values."
	return data 


if __name__ == "__main__":
	csvfile = sys.argv[1]
	geojsonfile = sys.argv[2]

	with open('updated_data.json', 'wb') as outfile:
		json.dump(append_properties_to_geojson(csvfile, geojsonfile), outfile, indent=4)

	print "Data dumped into 'updated_data.json'"





