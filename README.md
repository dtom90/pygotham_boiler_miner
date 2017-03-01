# pygotham_boiler
Code base for importing NYC boiler licence data from the NYC DOB BIS and the NYC DEP CATS.

The slides for a presentation describing this code can be found at [this link](https://docs.google.com/presentation/d/1hY2lQsHEirp1SxdUd9F1-WSxGsUWcq0QxQc5Pa5s4Eg/edit?usp=sharing).


###NYC DOB BIS Boiler Data:
Example in [test_DOB.py](https://github.com/dtom90/pygotham_boiler/blob/master/test_DOB.py) to get DOB Boiler data for a particular address:
```
from getDOBBoilerData import getDOBBoilerData

for line in getDOBBoilerData(1, "55", "Central Park West"):
    print(line)
```
NOTE: Due to server latency, this may need to be repeated a few times to work properly.

###NYC DEP CATS Boiler Data:
Example in [test_DEP.py](https://github.com/dtom90/pygotham_boiler/blob/master/test_DEP.py) to get the first 5 DEP boiler application records for each year from 1965-2015:
```
import storeDEPDataHTML
import writeDEPDataFiles
from getDEPData import getDEPData

print(getDEPData('CB000115'))
```
NOTE: This will take a while to complete
All DEP data is stored in ./DEPData