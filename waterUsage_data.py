import json
from urllib.request import urlopen
import pandas as pd
import requests
from datetime import datetime

url = "https://opendata.fcgov.com/resource/ia5t-gxxe.json"
data = pd.read_json(url)\

data.to_csv("Data/City_of_Fort_Collins_Water_Demand.csv")

  