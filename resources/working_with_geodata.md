
# Working with Geodata
----

The process for mapping something:

1. Decide what you want to show
2. Gather the data 
3. Get it in the format you need 
4. Map it!

Number 1 is up to you, number 4 we've been covering in detail. This guide deals with numbers 2 and 3. 

## Places to Find Data
<strong> Geospatial Data (things based on latlon coordinates) </strong>   
[Natural Earth](http://www.naturalearthdata.com/)  
[OpenStreetMap](https://www.openstreetmap.org/#map=5/48.879/11.294)   
[Mapzen](https://mapzen.com/data/metro-extracts) (For cities)   
[US Census](https://www.census.gov/geo/maps-data/)        
[Each US state](https://github.com/johan/world.geo.json/tree/master/countries)    
[Country Geo-boundaries](http://data.okfn.org/data/datasets/geo-boundaries-world-110m#data)
</br></bR>
<strong> Public Data </strong>   
[Enigma](http://enigma.io/)    
[This epic Quora answer](https://www.quora.com/Where-can-I-find-large-datasets-open-to-the-public)  
[US Census](https://www.census.gov/geo/maps-data/)     
</br>

## Getting data in the form you need
---
### Geospatial Data

If you're mapping geospatial things (states, countries, rivers, cities), you can have data in almost any format (CSV, GeoJson, KML, TopoJSON) as long as you use [Leaflet Omnivore](https://github.com/mapbox/leaflet-omnivore). See the `datafromcsv.html` example in the week3 folder.

### Adding non-geospatial data
If you're mapping something that doesn't have latlon coordinates, you'll likely want to use geojson and add it to the properties field. See the `states_popdensity.json` example in week3 folder. 

You can add this field to your geojson one of three ways. 

METHOD ONE: By hand. Add the values yourself. 

METHOD TWO: Programmatically, using [this code](https://github.com/MimiOnuoha/add-csv-values-to-geojson). 

METHOD THREE: By going to [geojson.io](geojson.io) and using the method we did in class: 

1. Drag in your original geojson file. You should see it appear on the map. 
2. Click the `Tables `tab, then the `+ new column`button. 
3. Name your new field, and enter in the necessary data.
4. In the top left, click the `Save` tab and choose `GeoJSON` as your option. 

METHOD FOUR: By writing your own code to do this. Feel free if you are able to! 

To validate or format geojson, use [jsonformatter](https://jsonformatter.curiousconcept.com/) or [jsonviewer](http://jsonviewer.stack.hu/) (the latter is better for huge datasets).

### Converting a shapefile or CSV to GeoJSON 

For Shapefiles: [Mapshaper](http://www.mapshaper.org/)    
For CSVs: [Ogre](https://ogre.adc4gis.com/) 

###  JSON to geoJSON
We can't technically say that we are converting GeoJSON to JSON because GeoJSON *is* JSON. It just is a type of JSON that has it's own particular format.  

Anyway, if you want to change JSON to GeoJSON, you can use the `jsonToGeo.py` code that is in the newly created Resources folder. 

If you don't know how to run a python module, skip to the "Working with Python" section below. 

If you do know how, read on: You will need to download the file and make sure it is in the same directory as your input json file. Then when you want to run it, you can do so like this:

		python jsonToGeo.py inputfile.json outputfile.json

Two things: 

1. Of course, you should change "inputfile" and "outputfile" to your input filename and what you want the geojson file name to me. (Also make sure the path ending matches yours.) See the example `samplejson.json` and `samplegeojson.json` for a sample before and after (NOTE: I deleted some data to make the files smaller, so the structure is correct, though they might not match exactly in terms of content).
2. jsonToGeo.py has simplejson as a dependency, so you'll probably want to install it using pip. If you don't know how to do that, skip to the below "Working with Python" section.

Once you have the geojson file, you should be able to include it on your leaflet map! 


-----

## Working with Python Modules
Your macbook comes with Python pre-installed, you just need to access it through the terminal. To see this, just type `python` into your terminal, and you'll see a python environment where you can write python code. To get out of this environment, type `exit()` or the `CTRL + D` keys

This isn't meant to teach you how to work with Python, there are plenty of other online tutorials for this. This will just give basics for how to use the `jsontoGeo.py` module so that you can change your JSON code to geoJSON format. 

- You will need to download the `jsontoGeo.py`file that is in the Resources folder and make sure it is in the same directory as the data you're working with.

- Go to your terminal window. The first thing you'll want to do is install pip. It's a package management system that will make it easy for you to install other python modules. Type this in terminal:

		pip install -U pip setuptools

	You can check to make sure this worked by simply typing `pip` into the terminal. If you get back something like `pip 1.5.6` (or any other numbers) you'll know your installation was successful. 

	If you get an error or see a message like `command not found`, then you might need to sudo your install command, which just means running it with higher security privileges. You will have to type the following:

		sudo pip install -U pip setuptools

	When prompted, enter your password. Note: you probably will not see anything on the screen while typing, this is just a security measure. 


- Now you need to install simplejson, which is a library that the `jsontoGeo.py` code depends on. To do this, type the following in terminal:
	
		pip install simplejson
	
	Again, if this doesn't work, you might need to sudo the command, i.e. add sudo in front of it, press enter, and type your password when prompted. 
	
-  Now use `cd` to navigate to the directory where the json data you're trying to convert is in. Run the code 

		python jsonToGeo.py inputfile.json outputfile.json

	You should change "inputfile" and "outputfile" to your input filename and what you want the geojson file name to me. (Also make sure the path ending matches yours.) See the example `samplejson.json` and `samplegeojson.json` for a sample before and after (NOTE: I deleted some data to make the files smaller, so the structure is correct, though they might not match exactly in terms of content). 	







		
		