import os
import pandas as pd

def extract_non_nan_data(folder_path, column_name):
    # Create an empty list to store the extracted data
    computed_data = []

    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV file
        if file_name.endswith('.csv'):
            # Construct the full path to the CSV file
            file_path = os.path.join(folder_path, file_name)
            
            # Read the CSV file into a pandas dataframe
            df = pd.read_csv(file_path)
            
            df['DATE'] = pd.to_datetime(df['DATE'])

            monthly_averages = df.groupby(df['DATE'].dt.to_period('M'))[column_name].mean()

            computed_data.extend(monthly_averages)


    # Write computed data to a text file
    with open(output_file, 'w') as f:
        for item in computed_data:
            f.write("%s\n" % item)
        
    return computed_data

folder_path = 'data'
field = 'DailyAverageWindSpeed'
output_file = 'process_output.txt'
computed_data = extract_non_nan_data(folder_path, field)
#print(computed_data)