import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Download and parse the HTML

tesla_url = "http://en.wikipedia.org/wiki/Tesla,_Inc"

# Download the HTML from tesla_url
tesla_html = requests.get(tesla_url)

# Parse the HTML with the BeautifulSoup and create a soup object
soup = BeautifulSoup(tesla_html.text, features='html.parser')

# Save a local copy
with open('tesla.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())

# Select table.wikitable
full_table = soup.select('table.wikitable tbody') [0]

# Extract the table column headings
# End result: A list with all the column headings

regex = re.compile('_\[\w\]')

table_head = full_table.select('th')
table_columns = []
for element in table_head:
    column_label = element.get_text(separator=" ", strip=True)
    column_label = column_label.replace(' ', '_')
    column_label = regex.sub('', column_label)
    table_columns.append(column_label)

table_rows = full_table.select('tr')

table_data = []
for index, element in enumerate(table_rows):
    if index > 0:
        row_list = []
        values = element.select('td')
        for value in values:
            row_list.append(value.text.strip())
        table_data.append(row_list)
#    print(column_label)
#print ('------------')
#print(table_data)

# Create a Pandas Dataframe
df = pd.DataFrame(table_data, columns=table_columns)
df

# Use the jupyter-lab command to launch jupyter lab local server and see the table you scraped.