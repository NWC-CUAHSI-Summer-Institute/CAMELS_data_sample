import os

def shorten_files_with_header(base_dir, keep_start, keep_end):
    # Walk through all directories and files in base_dir
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('_lump_nldas_forcing_leap.txt'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                
                # Read the file
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                
                # Keep the headers
                header = lines[:4]
                
                # Select the range of lines to keep, adjust indices for zero-based indexing
                main_content = lines[keep_start-1:keep_end]
                
                # Combine header and selected lines
                content_to_keep = header + main_content
                
                # Write the selected content back to the same file
                with open(file_path, 'w') as file:
                    file.writelines(content_to_keep)
                print(f"Updated {file_path}")

# Specify the base directory where the files are located
base_directory = '.'  # Adjust as necessary
start_keep = 5025
end_keep = 12334

# Call the function
shorten_files_with_header(base_directory, start_keep, end_keep)
