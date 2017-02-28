from bs4 import BeautifulSoup
import urllib.request
import os

siteBase = "https://a826-web01.nyc.gov/DEP.BoilerInformationExt/Home/Success/"
pathBase = os.path.join(os.path.dirname(__file__), 'DEPData/')
for year in range( 1965, 2016 ):
    siteEnd = str( year % 100 ).zfill( 2 )
    pathPrefix = ( pathBase + str( year // 100 ) + "xx/" +
                   str( year // 10 ) + "x/" + str( year ) + "/" )
    for i in range(1,5):
        if year < 2000:
            mySite = siteBase + "CA" + str( i ).zfill( 4 ) + siteEnd
            page = urllib.request.urlopen( mySite )
            soup = BeautifulSoup( page.read(), "html.parser" )
            filename = pathPrefix + "CA" + str( i ).zfill( 4 ) + siteEnd + ".html"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            f = open( filename, "w" )
            f.write( str( soup ) )
            f.close
        if year >= 2000:
            mySite = siteBase + "CB" + str( i ).zfill( 4 ) + siteEnd
            page = urllib.request.urlopen( mySite )
            soup = BeautifulSoup( page.read(), "html.parser" )
            filename = pathPrefix + "CB" + str( i ).zfill( 4 ) + siteEnd + ".html"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            f = open(filename, "w")
            f.write( str( soup ) )
            f.close
        if year > 2011:
            mySite = siteBase + "CR" + str( i ).zfill( 4 ) + siteEnd
            page = urllib.request.urlopen( mySite )
            soup = BeautifulSoup(page.read(), "html.parser")
            filename = pathPrefix + "CR" + str( i ).zfill( 4 ) + siteEnd + ".html"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            f = open(filename, "w")
            f.write( str( soup ) )
            f.close
        if year > 2014:
            mySite = siteBase + "CW" + str( i ).zfill( 4 ) + siteEnd
            page = urllib.request.urlopen( mySite )
            soup = BeautifulSoup( page.read(), "html.parser" )
            filename = pathPrefix + "CW" + str( i ).zfill( 4 ) + siteEnd + ".html"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            f = open(filename, "w")
            f.write( str( soup ) )
            f.close

