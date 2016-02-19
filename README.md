# Everything is Physical: The Art of Digital Mapping 

---

**Instructor**: Mimi Onuoha  
**Time**: Fridays 3:20 - 5:50 
</br>**Contact**: <cgo221@nyu.edu>
</br>**Office Hours**: [Calendar](https://calendar.google.com/calendar/selfsched?sstoken=UUl0bkJBeEw5QmpTfGRlZmF1bHR8MTVmMGJiY2ZkYjkyNWQ0NGQ1Y2YzODliMDQ0MmRlODU)

## Course Description

Digital technology has created new opportunities and resources for mapping, cartography, and geolocation-based visual investigation. It has also brought the need to consider issues concerning power, representation, and space. In this seven-week course, students will be introduced to GIS (geographical information system) basics and learn the practical realities of working with spatial data using digital mapping tools and technologies like mapshaper, Leaflet.js, TileMill, MapBox, and d3.js. Time will also be devoted to investigating the conceptual questions that inform mapping and strategies for counter-mapping. What makes a good map? 

Topics of discussion will include: what do maps represent as visual information artifacts? What happens when we consider maps as art objects? How is the expression of geodata a result of political processes? What does it mean for virtual creations to refer to physical realities, and in what ways do the two shape one another?
Students will work individually on weekly assignments, but will have the opportunity to collaborate on a final project that addresses the techniques and topics studied in the course. To get the most out of this course, students should already have a working understanding of HTML, CSS, and Javascript. This two-credit course will meet the first seven weeks of the semester.
Office hours are by appointment, and I'll stay for 20 minutes after every class if you have questions. 

#### Format
Each week will begin with a selection of students presenting assignment from previous week. If there was a reading assigned, the class will start with a brief discussion of it (no laptops open during discussion).  The bulk of the class will be spent introducing and experimenting with more technical mapping methods and tools.

#### Learning Objectives 
- Exposure to broad range of techniques in digital mapping (students should eventually focus on one or two)
- Become conversational in the topics that surround the theory and understanding of cartography and mapping space
- Create maps (or map-based objects) that work as art objects and challenge common conventions or understandings of the capabilities of maps.

#### Grading
Course marks will be determined by evaluating class participation (including showing up on time!), weekly assignments, and the final project. 


#### Other Resources
READINGS: There are extra texts in the readings folder that are **NOT** required for the course. They are provided as a further resource for students who are interested in delving deeper into mapping/cartography concepts. 


[Maptime's resources](http://maptime.io/lessons-resources/)
</br>[Ingrid Burrington's Overview of Mapping Tools](http://lifewinning.github.io/maps-cmu/resources/big-picture-tools.html)
</br>[Tom MacWright's Awesome Geojson](https://github.com/tmcw/awesome-geojson/blob/master/README.md)
</br> [A Random Assortment of Mapping Resources](https://docs.google.com/document/d/1YL4ypI32HBrkWCuycAdF3FHK-sGFfS9Zc949dgjMgB4/edit?usp=sharing)   
[William Whyte's *The Social Life of Small Urban Spaces*"](https://vimeo.com/111488563)  
[Mapping Realtime feeds with Mapbox](https://www.mapbox.com/mapbox.js/example/v1.0.0/live-data-marker/)



---

## Syllabus 
NOTE I: This syllabus is subject to change, and will be updated weekly. Bookmark and check often!

NOTE II: If a link for a reading isn't provided, then it can be found in the "Readings" directory. Do the readings! Most of them are short, and all of them are useful. The weekly folders contain all materials used in class and/or necessary for assignments. 

#### Week One - January 29
*About the course, logistics, and each other.* 

*What is a map? What's the history of mapping? How are maps used in ways that advance agendas? What are the tools involved in digital/web mapping, and what makes it different from its predecessors?* 

- Introductions
- Discussion / Viewing: What can mapping do?
- [Presentation](http://mimionuoha.github.io/digitalmapping/weekone/#/): a quick history of mapping; analog vs digital vs web; how web mapping works; what maps do* 
- Demonstration: A simple web map (Leaflet.js)**ASSIGNMENTS**:
- Read: "Mappings", Jeremy W. Crampton (from Wiley-Blackwell Companion to Cultural Geography)
- Create a map:
	- Change the [location](http://www.latlong.net/)
	- Use Leaflet.js, load tiles from [Stamen](http://maps.stamen.com/#toner-lite/12/37.7707/-122.3781), [CartoDB](https://cartodb.com/basemaps/) or any other basemap provider 
	- Push map online to your blog or github.io page and send me the link before Friday 
- Go through [this](http://maptime.io/anatomy-of-a-web-map/#0) 
#### Week Two - February 5
*Everything you need to know about tiles.*

*Where does geographic data come from? What forms does it take, how has it been used in the past? How should we think about it now?*


- Discussion of Reading + Assignments
- [Presentation](http://mimionuoha.github.io/digitalmapping/weektwo/#/): Tiles, tiles, tiles. GeoJSON and the data layer. Where geographic data comes from, why it matters.
- [Demonstration](https://www.dropbox.com/sh/yz2gafipzm6c744/AADTBTNQUmbHI4Tby3dtdjOca?dl=0): Adding data to our maps (tools: geojsonlint, Mapshaper, Mapzen, geojson.io). Getting data into the right format. 

**ASSIGNMENTS**:
- Reading: 
	- Borges & Baudrillard (in that order)
	- [When Google Goes Blind](http://www.atlasobscura.com/articles/investigating-censored-spots-on-google-earth) 
	- Add at least one geojson layer to your map(s): 
		- Use data that you have gathered from somewhere 
		- Add at least one marker or pop-up to your site 
		- NOTE: Think about what relationship/story/correlation (or lack thereof) you are trying to show. Why did you choose the data you did? 
		- Make sure map is online and send me the link BEFORE 1pm on Friday
#### Week Three - February 12
*An overview of map projections.*

*Dealing more with data, some overview of projections. If time: CartoDB and legends* 
<!--
*Dealing more with data. What sorts of things shouldn’t be mapped? How do you know if you’re clarifying or obscuring, and what are the uses of both?*-->
- Discussion + go over last week's reading- Last week's assignment
- [Presentation](http://mimionuoha.github.io/digitalmapping/weekthree/#/): more on geodata, projections, etc. - [Demonstration](https://www.dropbox.com/sh/n29t5q3a83z6w14/AABL2j_mux1lZdBOuMGEDdMta?dl=0): More on finding, converting, and working with data. 

**ASSIGNMENTS**:
-  Reading: 
	-  [How A Map is Like an Op-Ed](http://www.citylab.com/tech/2013/04/how-map-op-ed/5143/)
	- US Gov overview of the [Tehran Conference](https://history.state.gov/milestones/1937-1945/tehran-conf)
- Assignment:
	- Sign up for mapbox account [here](https://www.mapbox.com/education)	
	-  Make another map, or add more to your map from last week. Add a legend to your map, or a geosearch function, or a means of navigating/understanding your map. Create a complete map; make it so that someone could understand what you're representing if you weren't there to explain it.  

USEFUL: code for adding CSV values to geojson [here](https://github.com/MimiOnuoha/add-csv-values-to-geojson). 
#### Week Four - February 19*Visual Cues, Design Considerations. How can we use visual cues to tell stories? What are the traditional design rules of maps, and how can and should we interact with them?* 
- Discussion + last week's assignment- [Presentation](http://mimionuoha.github.io/digitalmapping/weekfour/#/11): quick using python modules, understanding Mapbox 
- Demonstration: Visual tools for thinking about maps. Tilemill, more on Mapbox, [ColorBrewer](http://colorbrewer2.org/)(and vice versa). 

**ASSIGNMENTS**:
- Reading: Trevor Paglen, *Experimental Geography* (in readings folder of repo)
	- Design and upload your own customized Mapbox layer. You can import your own data into it or choose to focus just on the tile layer. Upload it and send me the link. 
	- If you did not get the labels on your map working last week, send me the working version this week. 

#### Week Five - February 26
*Discussing final projects: expectations, presentation. Working with realtime data, Turf.js, other potentially useful Leaflet and Mapbox plugins. Quick overvie on mapping in D3.js.*- Discussion + last week's assignment- Viewing: Examples of maps that play with the limits of geography (aka, [inspiration](https://gist.github.com/lifewinning/b3603b1378b5fe560070) for final projects)- Presentation: Final project brief and requirements.- Demonstration: D3.js 

#### Week Six - March 4*Experimental Geography in practice. Guest presentations.* 
- [Very Brief] Overview/Discussion: Final project, final class.- Workshop: [Ann Chen](http://annhchen.com/whereabouts)- Speaker: [Josh Begley](https://joshbegley.com/)
#### Week Seven - March 11*Final Class* 
- Presenting Final Projects (featuring guest critics + museum studies students)
*Some slide images gratefully borrowed from the great folks at Maptime. 