import requests
import pandas as pd
import html5lib

url = 'https://www.allareacodes.com/area-code-list.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
result = requests.get(url, headers=headers)

response = result.text

# Parsing Table
data = pd.read_html(response)[0]
header = data.iloc[0]
data.columns = header
data = data[1:]

# Export as CSV
data.to_csv('area_codes.csv', sep='\t')