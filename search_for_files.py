import os

def search_for_basin_files(basin_id, nldas_src_dir, aorc_src_dir):
    # Prepare file paths based on expected patterns
    nldas_pattern = f"{basin_id}_hourly_nldas.csv"
    aorc_pattern = f"{basin_id}_1980_to_2024_agg_rounded.csv"

    # Search in NLDAS directory
    found_nldas = False
    for root, dirs, files in os.walk(nldas_src_dir):
        for file in files:
            if file == nldas_pattern:
                found_nldas = True
                print(f"NLDAS file for basin {basin_id} found at: {os.path.join(root, file)}")

    if not found_nldas:
        print(f"NLDAS file for basin {basin_id} not found in {nldas_src_dir}")

    # Search in AORC directory
    found_aorc = False
    for root, dirs, files in os.walk(aorc_src_dir):
        for file in files:
            if file == aorc_pattern:
                found_aorc = True
                print(f"AORC file for basin {basin_id} found at: {os.path.join(root, file)}")

    if not found_aorc:
        print(f"AORC file for basin {basin_id} not found in {aorc_src_dir}")


def main():
    # Load the list of basins from the sample_basins.txt file
    with open('sample_basins.txt', 'r') as f:
        basins = f.read().splitlines()

    # Define directories for NLDAS and AORC data
    nldas_src_dir = '/home/jmframe/data/CAMELS_US/hourly/nldas_hourly/'
    aorc_src_dir = '/home/jmframe/data/CAMELS_US/hourly/aorc_hourly/'

    # Search for each basin in both directories
    for basin in basins:
        print(f"\nSearching files for basin: {basin}")
        search_for_basin_files(basin, nldas_src_dir, aorc_src_dir)

if __name__ == "__main__":
    main()
