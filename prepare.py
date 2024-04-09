import os
import pandas as pd

def extract_non_nan_data(folder_path, column_name):
    # Create an empty list to store the extracted data
    extracted_data = []

    # Iterate through each file in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is a CSV file
        if file_name.endswith('.csv'):
            # Construct the full path to the CSV file
            file_path = os.path.join(folder_path, file_name)
            
            # Read the CSV file into a pandas dataframe
            df = pd.read_csv(file_path)
            
            # Extract non-NaN data from the specified column
            non_nan_data = df[column_name].dropna().tolist()
            
            # Append the extracted data to the list
            extracted_data.extend(non_nan_data)

    # Write extracted data to a text file
    with open(output_file, 'w') as f:
        for item in extracted_data:
            f.write("%s\n" % item)
        
    return extracted_data

folder_path = 'data'
field = 'AWND'
output_file = 'prepare_output.txt'
extracted_data = extract_non_nan_data(folder_path, field)
#print(extracted_data)
