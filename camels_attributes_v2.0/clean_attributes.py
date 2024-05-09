import os
import pandas as pd

def filter_gauge_ids(data_dir, gauge_list_file):
    # Load gauge IDs from the list file
    with open(gauge_list_file, 'r') as file:
        gauge_ids = set(line.strip() for line in file.readlines())
    
    # List all data files in the directory
    data_files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
    
    for data_file in data_files:
        file_path = os.path.join(data_dir, data_file)
        
        # Read the data file using pandas assuming semi-colon delimited
        data = pd.read_csv(file_path, delimiter=';', dtype={'gauge_id': str})
        
        # Filter the dataframe to only include rows with gauge_id in the list
        filtered_data = data[data['gauge_id'].isin(gauge_ids)]
        
        # Save the filtered data back to the file or a new file
        # Consider saving to a new file or creating backups if necessary
        filtered_data.to_csv(file_path, sep=';', index=False)
        print(f'Filtered {data_file} and saved.')

# Usage
data_directory = './camels_attributes_v2.0'
gauge_list_path = './sample_basins.txt'
filter_gauge_ids(data_directory, gauge_list_path)
