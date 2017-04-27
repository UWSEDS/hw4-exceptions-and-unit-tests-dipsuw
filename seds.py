# Importing the required libraries
import os
import requests
import zipfile
import pandas as pd

def get_data(url):
	try:
		if os.path.exists(url.split('/')[-1]):
			return 100
		else:
			req=requests.get(url)
			assert req.status_code == 200
			with open(url.split('/')[-1],'wb') as af:
				af.write(req.content)
		return 200
	except:
		return 404
	
#get_data('https://data.seattle.gov/resource/4xy5-26gy.csv')

def remove_data(url):
    if os.path.exists(url.split('/')[-1]):
        os.remove(url.split('/')[-1])
    else:
        print("File does not exist")
    return    	
	
#remove_data('https://data.seattle.gov/resource/4xy5-26gy.csv')	