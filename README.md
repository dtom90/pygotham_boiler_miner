# pygotham_boiler
Code base for importing NYC boiler licence data from the NYC DOB BIS and the NYC DEP CATS.

The slides for a presentation describing this code can be found at [this link](https://docs.google.com/presentation/d/1hY2lQsHEirp1SxdUd9F1-WSxGsUWcq0QxQc5Pa5s4Eg/edit?usp=sharing).


###Modifications by dtom90:
All DEP data is now stored in ./DEPData

To get DOB Boiler data for a particular address:
```
from getDOBBoilerData import getDOBBoilerData
getDOBBoilerData( boroNum, houseNum, houseStreet )
```

To get the first 5 DEP boiler application records for each year:
```
python3 storeDEPDataHTML.py
python3 writeDEPDataHTML.py
```