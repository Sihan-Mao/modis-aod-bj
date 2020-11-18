# use python 2.7 version for urlopnener
import os
import urllib
import pandas as pd

os.chdir('D:\\Auguste\\UChicago\\2018-2019\\2019winter\\GIS2\\project\\affordable-housing')
query = pd.read_csv('LAADS_query.csv')
url = query['fileUrls']

for path in url:
    webpath = 'https://ladsweb.modaps.eosdis.nasa.gov' + path
    filename = path[36:]
    filepath = os.path.join('D:\\Auguste\\UChicago\\2018-2019\\2019winter\\GIS2\\project\\hdf', filename)
    temp = urllib.URLopener()
    temp.retrieve(webpath, filepath)


