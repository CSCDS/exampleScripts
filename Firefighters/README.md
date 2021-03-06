
Firefighter interventions in Montreal
=======================================

# Description #  
Data set listing the interventions carried out by the Montreal Fire Safety Service (MIS), including rentals of interventions and units deployed since 2005. These data are taken from the Workstation Assisted Distribution (CAD) system. The central system of the management system interventions that allows real-time management, distribution of vehicles and operational monitoring of interventions. This data is collected to produce reports required by the Ministry of Public Security and necessary for the SIM. It also compiles statistics to disseminate information to citizens and the media.

### Year ###
2005 onwards

### Data ###
This dataset consists of three files:
 
  * [donneessouvertes-interventions-sim.csv](https://s3.ca-central-1.amazonaws.com/datascapes2017/Firefighters/donneesouvertes-interventions-sim.csv)
  * [donneessouvertes-interventions-sim-2005-2014.csv](https://s3.ca-central-1.amazonaws.com/datascapes2017/Firefighters/donneesouvertes-interventions-sim-2005-2014.csv)
  * [type-interventions-descriptions20161122.csv](https://s3.ca-central-1.amazonaws.com/datascapes2017/Firefighters/type-interventions-descriptions20161122.csv)

## Data Dictionary ##

### 1. donneessouvertes-interventions-sim.csv ###
| Column name | Description |
|-------------|-------------|
| __incident_nbr__ | identifying the event by year.|
| __creation_date_time__ | date and time of the event.|
| __description_groupe__ | grouping of types of interventions in 6 categories: Building fires, Other fires, Without fire, Fire alarms, First responders, False alerts / cancellations. |
| __incident_type_desc__ |type of incident|
| __caserne__ |number of the barracks responsible for the territory where the event occurred.|
| __nom_ville__ | Name of the city where the event occurred.|
| __nom_arrond__ | Name of the district where the event occurred.|
| __division__ | number of the MIS division responsible for the territory where the event occurred.|
| __latitude,longitude__ | geographical position of the event after obfuscation at an intersection according to the WGS84 geodesic datum. |
| __nombre_unites__ |number of vehicles deployed to respond to the event. A unit can consist of 3 to 5 firefighters.|

### 2. donneessouvertes-interventions-sim-2005-2014.csv ###

| Column name | Description |
|-------------|-------------|
| __INCIDENT_NBR__ | identifying the event by year.|
| __CREATION_DATE_TIME__ | date and time of the event.|
| __DESCRIPTION_GROUPE__ | grouping of types of interventions in 6 categories: Building fires, Other fires, Without fire, Fire alarms, First responders, False alerts / cancellations. |
| __INCIDENT_TYPE_DESC__ |type of incident|
| __CASERNE__ |number of the barracks responsible for the territory where the event occurred.|
| __NOM_VILLE__ | Name of the city where the event occurred.|
| __NOM_ARROND__ | Name of the district where the event occurred.|
| __DIVISION__ | number of the MIS division responsible for the territory where the event occurred.|
| __LONGITUDE,LATITUDE__ | geographical position of the event after obfuscation at an intersection according to the WGS84 geodesic datum. |
| __NOMBRE_UNITES__ |number of vehicles deployed to respond to the event. A unit can consist of 3 to 5 firefighters.|


### 3. type-interventions-descriptions20161122.csv ###


| Column name | Description |
|-------------|-------------|
| __INCIDENT_TYPE_DESCRIPTION__ |type of incident|
| __Description__ | Description of the incident |


[More information about field values](http://donnees.ville.montreal.qc.ca/dataset/interventions-service-securite-incendie-montreal)
