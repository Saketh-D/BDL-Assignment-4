import os
import yaml
import pandas as pd
from bs4 import BeautifulSoup
import sys
import random

# reading params.yaml
file_path = "params.yaml"

with open(file_path, 'r') as file:
    params = yaml.safe_load(file)

#print(params)

# URL of the file to download
url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/" + str(params['year'])

# Directory where you want to save the downloaded file
output_file = "/home/saketh/Desktop/assignment4/page.html"

# Use os.system() to execute wget command
command = f"wget -O {output_file} {url} -q"

# Execute the command
os.system(command)

def extract_csv_links(html_file):
    # Load the HTML file
    with open(html_file, 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all anchor tags (links)
    links = soup.find_all('a')

    # Extract href attribute from each link
    csv_links = []
    for link in links:
        href = link.get('href')
        # Check if the link ends with '.csv'
        if href.endswith('.csv'):
            csv_links.append(href)

    return csv_links


html_file = 'page.html'
csv_links = extract_csv_links(html_file)
#print(csv_links)
#print("length : ", len(csv_links))
random.shuffle(csv_links)

if params['n_locs'] > len(csv_links) :
    print("Number of locations is too high")
    sys.exit()


def delete_csv_files(folder_path):
    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV file
        if file_name.endswith('.csv'):
            # Construct the full path to the CSV file
            file_path = os.path.join(folder_path, file_name)
            # Delete the CSV file
            os.remove(file_path)


folder_path = 'data'

if os.path.exists(folder_path):
    delete_csv_files(folder_path)
else:
    os.makedirs(folder_path)

field = ['DailyAverageWindSpeed', 'AWND']
files_links = []

for i in range(len(csv_links)):
    link = url + "/" + csv_links[i]
    df = pd.read_csv(link)

    if df[field[0]].count() > 0 and df[field[1]].count() == 12:
        files_links.append(csv_links[i])

    if len(files_links) == params['n_locs']:
        break


for i in range(len(files_links)):
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/" + str(params['year']) + "/" + files_links[i] 
    output_file = "/home/saketh/Desktop/assignment4/data/" + files_links[i]
    command = f"wget -O {output_file} {url} -q"
    os.system(command)


"""
fields = ['Altimeter', 'DewPointTemperature', 'DryBulbTemperature', 'Precipitation',
'PresentWeatherType', 'PressureChange', 'PressureTendency', 'RelativeHumidity', 'SkyConditions',
'SeaLevelPressure', 'StationPressure', 'Visibility', 'WetBulbTemperature', 'WindDirection', 'WindGustSpeed',
'WindSpeed', 'Sunrise', 'Sunset']
"""