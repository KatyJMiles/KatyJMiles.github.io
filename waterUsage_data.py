import json
from urllib.request import urlopen
import pandas as pd
import requests
from datetime import datetime

from statsmodels.tsa.seasonal import STL

data = pd.read_csv("water_data.csv")
stl = STL(data["Total Actual Demand (MGD)"], seasonal=13, period = 12)
res = stl.fit()
fig = res.plot()
print(fig)

  