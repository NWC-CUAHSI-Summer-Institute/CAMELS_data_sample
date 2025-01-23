import os
import pandas as pd

# Paths
streamflow_src_dir = '/home/jmframe/data/CAMELS_US/hourly/usgs_streamflow/'
streamflow_dest_dir = './hourly/usgs_streamflow/'
sample_basins_file = 'sample_basins.txt'

# Create destination directory if it doesn't exist
os.makedirs(streamflow_dest_dir, exist_ok=True)

# Use the dates from the known daily file (same as before)
known_daily_file = './basin_mean_forcing/nldas/01/01013500_lump_nldas_forcing_leap.txt'
print(f"Using dates from daily file: {known_daily_file}")

try:
    df_daily = pd.read_csv(known_daily_file, delim_whitespace=True, skiprows=3, parse_dates={'date': ['Year', 'Mnth', 'Day']})
    daily_start_date = df_daily['date'].min()
    daily_end_date = df_daily['date'].max()
    print(f"  Daily file dates: {daily_start_date} to {daily_end_date}")
except Exception as e:
    print(f"Error reading known daily file: {e}")
    exit()

# Read the sample basins
with open(sample_basins_file, 'r') as f:
    basin_ids = f.read().splitlines()

# Process each basin
for basin_id in basin_ids:
    print(f"\nProcessing streamflow data for basin: {basin_id}")
    
    # Define paths for source and destination files
    streamflow_src_file = os.path.join(streamflow_src_dir, f"{basin_id}-usgs-hourly.csv")
    streamflow_dest_file = os.path.join(streamflow_dest_dir, f"{basin_id}-usgs-hourly.csv")
    
    # Process streamflow data
    if os.path.exists(streamflow_src_file):
        print(f"Found streamflow file for basin {basin_id}: {streamflow_src_file}")
        try:
            df_streamflow = pd.read_csv(streamflow_src_file, parse_dates=['date'], index_col='date')
            df_streamflow_truncated = df_streamflow[(df_streamflow.index >= daily_start_date) & (df_streamflow.index <= daily_end_date)]
            df_streamflow_truncated.to_csv(streamflow_dest_file)
            print(f"Streamflow data for basin {basin_id} truncated and saved to: {streamflow_dest_file}")
        except Exception as e:
            print(f"Error processing streamflow file for basin {basin_id}: {e}")
    else:
        print(f"Error: Streamflow file for basin {basin_id} not found at: {streamflow_src_file}")
