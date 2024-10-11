import os
import pandas as pd

# Paths
nldas_src_dir = '/home/jmframe/data/CAMELS_US/hourly/nldas_hourly/'
aorc_src_dir = '/home/jmframe/data/CAMELS_US/hourly/aorc_hourly/'
nldas_dest_dir = './hourly/nldas_hourly/'
aorc_dest_dir = './hourly/aorc_hourly/'
sample_basins_file = 'sample_basins.txt'

# Create destination directories if they don't exist
os.makedirs(nldas_dest_dir, exist_ok=True)
os.makedirs(aorc_dest_dir, exist_ok=True)

# Use the dates from a known daily file
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
    print(f"\nProcessing files for basin: {basin_id}")
    
    # Define paths for source files
    nldas_src_file = os.path.join(nldas_src_dir, f"{basin_id}_hourly_nldas.csv")
    aorc_src_file = os.path.join(aorc_src_dir, f"{basin_id}_1980_to_2024_agg_rounded.csv")
    
    # Define paths for destination files
    nldas_dest_file = os.path.join(nldas_dest_dir, f"{basin_id}_hourly_nldas.csv")
    aorc_dest_file = os.path.join(aorc_dest_dir, f"{basin_id}_1980_to_2024_agg_rounded.csv")
    
    # Process NLDAS hourly data
    if os.path.exists(nldas_src_file):
        print(f"Found NLDAS hourly file for basin {basin_id}: {nldas_src_file}")
        try:
            df_nldas = pd.read_csv(nldas_src_file, parse_dates=['date'], index_col='date')
            df_nldas_truncated = df_nldas[(df_nldas.index >= daily_start_date) & (df_nldas.index <= daily_end_date)]
            df_nldas_truncated.to_csv(nldas_dest_file)
            print(f"NLDAS hourly data for basin {basin_id} truncated and saved to: {nldas_dest_file}")
        except Exception as e:
            print(f"Error processing NLDAS file for basin {basin_id}: {e}")
    else:
        print(f"Error: NLDAS file for basin {basin_id} not found at: {nldas_src_file}")
    
    # Process AORC hourly data
    if os.path.exists(aorc_src_file):
        print(f"Found AORC hourly file for basin {basin_id}: {aorc_src_file}")
        try:
            df_aorc = pd.read_csv(aorc_src_file, parse_dates=['time'], index_col='time')
            df_aorc_truncated = df_aorc[(df_aorc.index >= daily_start_date) & (df_aorc.index <= daily_end_date)]
            df_aorc_truncated.to_csv(aorc_dest_file)
            print(f"AORC hourly data for basin {basin_id} truncated and saved to: {aorc_dest_file}")
        except Exception as e:
            print(f"Error processing AORC file for basin {basin_id}: {e}")
    else:
        print(f"Error: AORC file for basin {basin_id} not found at: {aorc_src_file}")
