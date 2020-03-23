# Tableau

Tableau is a data visualization software great for conducting visual analysis and displaying findings with visual aid.  

Tableau Public makes use of hybrid cloud/local computing.  Your data is stored on the cloud and workbooks you make on your account can be accessed anywhere there is a Tableau Desktop or Tableau Public application.  

[Download Tableau Public](https://public.tableau.com/en-us/s/download)

**Bonus**: You get a sweet profile to display all your visualizations.

**Drawback**: Public is not recommended for sensitive data.
	Tableau Public can also demand a lot of your local resources as large data transformations and calculations will quickly eat up much of your local resources and leave your computer lagging around. I've also noticed an issue with it interpreting the 'Pages' aspects of visualizations.

Importing data is very simple and can come from a variety of formats such as csv, excel or json.  Be mindful of excel files because they have a mind of their own and tend to ‘interpret’ data and assign them best guess data types.  These best guesses can sometimes change the data.  Tableau is also smart and can interpret datatypes and assign a best guess, but it also takes into consideration Excel when reading in an Excel file.

#### Tableau Datatypes
- Integer (Decimal & Whole)
- Boolean
- Date & Time: 2016:12:05 09:30:00
- Date: 2016:05 or January 2016 or 01:2017:01
- String
- Geographic - These can be anything from Longitude and Latitude Coordinates, Zip codes, City names, Counties, States, Countries. (*Very, Very Helpful.  We will bring this all home during TimeSeries week*)

### Tableau Creative Spaces

**Sheets** - workspace to build and finalize visualizations and for presenting results or exploratory analysis.

**Dashboards** - Combinations of 1 or more finalized visualizations.  Very useful is you want to combined different graphs/visualizations that utilize similar filtering/sorting.

**Stories** - Collection of finalized visualizations or dashboards.  Dashboards are made of one or more pages, with each page being an individual sheet or dashboard.  These are great for presenting several visualizations, ideally of a related topic.  You can even go as far as make full presentations out of these stories.

### Visualization

#### Pills (Those Draggy-Droppy bits)
- **Measures** Any feature that is described quantitatively.
- **Dimensions** Any feature that is described qualitatively.

**Table Calculations**
Table Calculations are similar in offerings to the Quick Table Calculations, however they contain more customization options.

**Calculated Fields** -
Calculate Fields are basically a way to Engineer Features in Tableau.  They function very similar to Excel table Calculations.

**Aggregate Measures.** -
When plotting measures against measures Tableau has a Tendency to Aggregate measures, or collectively summarize all observations as a single point. A lot of times you are going to create a viz and it will end up as a single observation. If this ever happens check the ‘Aggregate Measures’ option in the Analysis tab.


## Tableau exercises

### Using sat_2017_final.csv

- **Which four states have the highest math score?**
  - Try sorting the data in a bar chart
  - Add a filter to all states above 630

- **Can we make a scatter plot comparing Participation to evidence based reading and writing?**
  - Remove zero from the axis
  - Add a title  

- **Create a "choropleth" map of the country of total scores**
    - can we compare participation to total score?
    - Use the "show me" tab on the top right
    - Filter to the lower 48

- **Create a Dashboard comparing participation to score**
  - Naming your sheets will make them easier to track
  - Title your charts!

### Using the UFO csv
- **Investigate the relationship between time of year and ufo sightings**

- **How have ufo sightings changed since the 30s?**

- **Try creating a map of the United States that shows UFO sightings over time.
You can animate your visualization by including year in the `pages` feature.**


### Using the NYC-Leading-Causes-of-Death dataset

- **What are the leading causes of death in New York (according to our data)?**
  - BONUS:  Research what is the common description of the second leading cause of death.

- **What is the Second leading cause of death in New York in 2010?**
  - Filters or Pages may help

- **What percent of all deaths recorded are attributed to the leading cause of deaths?**
  - Use a Quick Table Calculation

- **Which Causes of Death are Males more at risk for as opposed to females and vise versa?**



#### Feel free to continue exploring the datasets and creating visualizations - Tableau is a powerful tool!
