#!/usr/bin/python
import csv
import os
from getDEPData import *

outputPathBase = os.path.join(os.path.dirname(__file__), 'DEPData/')
urlBase = "file://"+outputPathBase

def tryAndAddDEPApplication( urlPrefix, appPrefix, i, urlSuffix, data ):
    url = urlPrefix + appPrefix + str(i).zfill(4) + urlSuffix
    print(url)
    try:
        soup = urlToSoup(url)
        if hasDEPData( soup ):
            print( appPrefix, str(i).zfill(4), appYearYY, sep = '')
            data.writerow( extractDEPDataFromSoup(soup) )
    except:
        pass

for appYear in range( 1965, 2016 ):

    appYearYYxx = str( appYear // 100 ) + "xx"
    appYearYYYx = str( appYear // 10  ) + "x"
    appYearYY   = str( appYear %  100 ).zfill(2)

    outputPath = outputPathBase
    urlPrefix = urlBase + appYearYYxx + "/" + appYearYYYx + "/" + str(appYear) + "/"
    urlSuffix = appYearYY + ".html"

    f = open(outputPath + "Applications" + str(appYear) + ".csv", "w", newline = '')
    data = csv.writer(f)
    data.writerow(["Building Address", "Boro", "BIN", "Block", "Lot",
                "Owner", "Application Number", "Application Type",
                "Expiration Date", "Business Type", "Request Type",
                "Application Status", "Submitted Date", "Decision Date",
                "Boiler Make and Model", "Primary Fuel", "Secondary Fuel",
                "Heat Input", "Burner Make and Model", "Number of Identical Units",
                "Building Alias"])

    for i in range(1,5):
        
        if appYear < 2000:
            tryAndAddDEPApplication( urlPrefix, "CA", i, urlSuffix, data )
        else:
            tryAndAddDEPApplication( urlPrefix, "CB", i, urlSuffix, data )
            if appYear > 2011:
                tryAndAddDEPApplication( urlPrefix, "CR", i, urlSuffix, data )
                if appYear < 2015:
                    tryAndAddDEPApplication( urlPrefix, "CW", i, urlSuffix, data )
    del data
    f.close()
